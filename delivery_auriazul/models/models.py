from odoo import models, fields, api

class Deliveryauriazul(models.Model):
    _inherit = "stock.picking"
    km = fields.Char (string= "Km estimado")
    fecha_inicio = fields.Datetime (string= "Fecha inicio traslado")
    fecha_fin = fields.Datetime (string= "Fecha fin traslado")
    chofer= fields.Char(string="Chofer")
    motivo_traslado= fields.Char(string="Motivo de traslado")
    numero_remision= fields.Char(string="Número de remisión")




