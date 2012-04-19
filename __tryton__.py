# -*- coding: utf-8 -*-
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'Project GTD',
    'version': '2.3.0',
    'author': 'Sergi Almacellas Abellana',
    'email': 'sergi@koolpi.com',
    'website': 'http://www.tryton.org/',
    'description': '''Getting Thinks Done Implementation''',
    'depends': [
        'ir',
        'project',
    ],
    'xml': [
        'project_gtd.xml',
    ],
    'translation': [
        'locale/ca_ES.po',
        'locale/es_ES.po',
    ],
}
