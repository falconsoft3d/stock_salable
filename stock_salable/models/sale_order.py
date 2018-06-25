# coding: utf-8
from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    qty_salable = fields.Float('Stock Salable', compute='_compute_qty_salable', store=True)

    @api.one
    @api.depends('product_id', 'order_id')
    def _compute_qty_salable(self):
        self.qty_salable = sum(self.product_id.stock_quant_ids.filtered(lambda q: q.location_id.salable_stock and not q.reservation_id and q.location_id == self.order_id.warehouse_id.lot_stock_id).mapped('qty')) if getattr(self.order_id, 'warehouse_id') else self.product_id.qty_salable
