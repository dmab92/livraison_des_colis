# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class colis_app(models.Model):
#     _name = 'colis_app.colis_app'
#     _description = 'colis_app.colis_app'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
