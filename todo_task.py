# -*- coding: utf-8 -*-
from openerp import models, fields, api
class TodoTask(models.Model):
	name = fields.Char(help="What needs to be done?")
	_name = 'todo.task'
	_inherit = ['todo.task', 'mail.thread']
	# _inherit = 'todo.task'
	user_id = fields.Many2one('res.users', 'Responsible')
	date_deadline = fields.Date('Deadline')

class User(models.Model):
	_name = 'res.users'
	_inherits = {'res.partner': 'partner_id'}
	partner_id = fields.Many2one('res.partner')