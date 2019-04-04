# Copyright (C) 2013-2014 GRAP (http://www.grap.coop)
# @author Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models
from odoo.tools import safe_eval


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    @api.model
    def get_default_auth_admin_passkey_send_to_admin(self):
        ICPSudo = self.env['ir.config_parameter'].sudo()
        return safe_eval(ICPSudo.get_param(
            'auth_admin_passkey.send_to_admin',
            default=False
        ))

    @api.model
    def get_default_auth_admin_passkey_send_to_user(self):
        ICPSudo = self.env['ir.config_parameter'].sudo()
        return safe_eval(ICPSudo.get_param(
            'auth_admin_passkey.send_to_user',
            default=False
        ))

    auth_admin_passkey_send_to_admin = fields.Boolean(
        'Send email to admin user.',
        help=('When the administrator use his password to login in '
              'with a different account, Odoo will send an email '
              'to the admin user.'),
    )
    auth_admin_passkey_send_to_user = fields.Boolean(
        string='Send email to user.',
        help=('When the administrator use his password to login in '
              'with a different account, Odoo will send an email '
              'to the account user.'),
    )

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            auth_admin_passkey_send_to_admin=self.get_default_auth_admin_passkey_send_to_admin(),
            auth_admin_passkey_send_to_user=self.get_default_auth_admin_passkey_send_to_user()
        )
        return res

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        ICPSudo.set_param('auth_admin_passkey.send_to_admin', repr(self.auth_admin_passkey_send_to_admin))
        ICPSudo.set_param('auth_admin_passkey.send_to_user', repr(self.auth_admin_passkey_send_to_user))