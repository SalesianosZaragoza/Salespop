# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api

class Persona(models.Model):
    _name = 'salespop.persona'
    name = fields.Char('Nombre')
    direction = fields.Char('Direccion')
    telefono = fields.Char('Telefono')


class Estudiante(models.Model):
    _inherit = 'salespop.persona'
    _name = 'salespop.estudiante'
    portatiles_id = fields.One2many('salespop.portatil', 'comprador_id', string='Portatiles')

class Portatil(models.Model):
    _name = 'salespop.portatil'
    name = fields.Char('Modelo')
    marca = fields.Char('Marca')
    cpu = fields.Char('CPU')
    ram_id = fields.One2many('salespop.ram', 'portatil_id', string='RAM')
    hdd_id = fields.One2many('salespop.hdd', 'portatil_id', string='HDD')
    fecha_compra = fields.Date('Fecha de Compra')
    usage = fields.Float('Usage')
    comprador_id = fields.Many2one('salespop.comprador', string='Comprador')
    precio = fields.Float('Precio')
    observaciones = fields.Text('Observaciones')
    total_ram = fields.Float('Total RAM')
    total_hdd = fields.Float('Total HDD')
    ofertas_id = fields.One2many('salespop.oferta', 'portatil_id', string='Oferta')
    vendido = fields.Boolean('Vendido')


class RAM(models.Model):
    _name = 'salespop.ram'
    name = fields.Char('Nombre')
    frecuencia = fields.Integer('Frecuencia')
    latencia = fields.Char('Latencia')
    cantidad = fields.Integer('Cantidad GB')
    tipo = fields.Selection([('DDR', 'DDR'), ('DDR2', 'DDR2'), ('DDR3', 'DDR3')], string='Tipo')
    portatil_id = fields.Many2one('salespop.portatil', string='Portatil')


class HDD(models.Model):
    _name = 'salespop.hdd'
    name = fields.Char('Nombre')
    capacidad = fields.Integer('Capacidad')
    tipo = fields.Selection([('SSD', 'SSD'), ('HDD', 'HDD')], string='Tipo')
    portatil_id = fields.Many2one('salespop.portatil', string='Portatil')


class Comprador(models.Model):
    _inherit = 'salespop.persona'
    _name = 'salespop.comprador'
    portatiles_id = fields.One2many('salespop.portatil', 'comprador_id', string='Portatiles')
    ofertas_id = fields.One2many('salespop.oferta', 'comprador_id', string='Ofertas')


class Oferta(models.Model):
    _name = 'salespop.oferta'
    name = fields.Char('Nombre')
    portatil_id = fields.Many2one('salespop.portatil', string='Portatil')
    aceptada = fields.Boolean('Aceptada')
    comprador_id = fields.Many2one('salespop.comprador', string='Comprador')
    observaciones = fields.Text('Observaciones')