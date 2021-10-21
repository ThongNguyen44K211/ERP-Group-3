from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class SalesModule(models.Model):
    _name = "Sales.Vinamilk"
    _description = "Managing Milks information"

    name = fields.Char('Milks Name', required=True)
    type = fields.char('Type')
    description = fields.Text('Milks Description')
    capacity = fields.Integer('Capacity Milk', default=1)
    Quanity = fields.Integer('Quanity')
    Price = fields.Float('Quanity', default=1)
    Status = fields.Selection([
        ('Available', 'UnAvailable'),
        ('Available', 'UnAvailable')
    ], string='Status', default='Available')
    Milks_image = fields.Binary("Milks Image", attachment=True, help="Milks Image")
    owner_id = fields.Many2one('res.partner', string='Owner')
    product_ids = fields.Many2many(comodel_name='product.product',
                                string="Related Products",
                                relation='Milks_product_rel',
                                column1='col_Milks_id',
                                column2='col_product_id')