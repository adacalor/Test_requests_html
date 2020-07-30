# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:26:43 2020

@author: Collabcap
"""

from requests_html import HTMLSession
session = HTMLSession()


r = session.get('https://www.collaborationcapital.org/mentions-legales', timeout=10)

print( r.html.render() )
