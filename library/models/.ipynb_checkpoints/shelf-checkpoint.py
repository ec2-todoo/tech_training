# -*- coding: utf-8 -*-

from odoo import models, fields

class LibraryTags(models.Model):
    _name = 'library.tags'
    _description ='Library book Tags'

    name = fields.Char(string='Name')

class Library(models.Model):
     _name = 'library.shelf'
     _description = 'Library Shelf'

     name = fields.Char(string='Book Title', required=True, index=True, help='Ingrese el nombre del libro')
     description = fields.Html(string='Description')
     banner = fields.Binary(string='Banner')
     price = fields.Float(string='Price', digits=(5, 4))

    expire_date = fields.Date(string='Expire After', required=True)
    
    responsible_id = fields.Many2one(comodel_name='res.users', required=True,
                        string='Responsible', ondelete='restrict', copy=False)
    
    tag_ids = fields.Many2many(comodel_name='library.tags', relation='rel_book_tags',
                            column1='book_id', column2='tag_id', string='Tags')
    #     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
