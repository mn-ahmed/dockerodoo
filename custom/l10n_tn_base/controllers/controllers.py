# -*- coding: utf-8 -*-
# from odoo import http


# class L10nTnBase(http.Controller):
#     @http.route('/l10n_tn_base/l10n_tn_base', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_tn_base/l10n_tn_base/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_tn_base.listing', {
#             'root': '/l10n_tn_base/l10n_tn_base',
#             'objects': http.request.env['l10n_tn_base.l10n_tn_base'].search([]),
#         })

#     @http.route('/l10n_tn_base/l10n_tn_base/objects/<model("l10n_tn_base.l10n_tn_base"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_tn_base.object', {
#             'object': obj
#         })
