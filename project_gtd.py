# -*- coding: utf-8 -*-
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Eval

class Context(ModelSQL,ModelView):
    'GTD Context'
    _name = 'task.context'
    __description__ = __doc__
    sequence = fields.Integer('Sequence')
    name = fields.Char('Name', required=True)

Context()

class Priority(ModelSQL,ModelView):
    'GTD Priority'
    _name = 'task.priority'
    __description__ = __doc__
    sequence = fields.Integer('Sequence')
    name = fields.Char('Name', required=True)

Priority()

class Work(ModelSQL, ModelView):
    'Work Effort'
    _name = 'project.work'
    
    context = fields.Many2One('task.context', 'Context', 
                states={
                'invisible': Eval('type') != 'task',
                }, depends=['type'])
    priority = fields.Many2One('task.priority', 'Priority', 
                states={
                'invisible': Eval('type') != 'task',
                }, depends=['type'])
    
Work()
