# -*- coding: utf-8 -*-

from odoo import models, fields

class Library(models.Model):
     _name = 'library.shelf'
     _description = 'library Shelf'

     name = fields.Char(string='Book Title', required=True, index=True, index=True, help='Ingrese el nombre del libro')
     description = fields.Html(string='Description')
     banner = fields.Binary(string='Banner')
     price = fields.Float(string='Price', digits=(5, 4))
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
