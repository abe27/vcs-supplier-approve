# -*- coding: utf-8 -*-
# from odoo import http


# class SupplierApprove(http.Controller):
#     @http.route('/supplier_approve/supplier_approve', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/supplier_approve/supplier_approve/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('supplier_approve.listing', {
#             'root': '/supplier_approve/supplier_approve',
#             'objects': http.request.env['supplier_approve.supplier_approve'].search([]),
#         })

#     @http.route('/supplier_approve/supplier_approve/objects/<model("supplier_approve.supplier_approve"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('supplier_approve.object', {
#             'object': obj
#         })
