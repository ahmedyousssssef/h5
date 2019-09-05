# -*- coding: utf-8 -*-
from openerp import models, fields, api, _

class OrgChartDepartment(models.Model):
	_name = 'organiztion.chart'
	_rec_name = 'name'

	name = fields.Char(default="Org Chart Department")

	department_id = fields.Many2one('hr.department', string='Department', store=True)
	manager_id = fields.Many2one(string="Department Manager" , related='department_id.manager_id')
	# employee_id = fields.Many2one('hr.employee', string="Department Manager" , related='department_id.manager_id' , store=True)
	employee_id = fields.Many2one('hr.employee', string="Employee" , store=True)

	@api.onchange('department_id')
	def onchange_department_id(self):
		self.employee_id = self.manager_id

	@api.multi
	def get_full_organizationchart(self):
		print("kokokokok")
		ceo = self.env['hr.job'].search([('name' , '=' , 'CEO')]).id
		self.employee_id = self.env['hr.employee'].search([('job_id' , '=' , ceo)]).id

