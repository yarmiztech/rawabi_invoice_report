from odoo import models,fields,api

class AccountMove(models.Model):
    _inherit = 'account.move'

    def total_amount_untaxed(self):
        taxable_amount = 0.00
        for amt in self.invoice_line_ids:
            if amt.discount != 0.00:
                taxable_amount+= amt.quantity * amt.price_unit
        return '%.2f' % taxable_amount






class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    def price_subtotal_line(self):
        taxable_amount = 0.00
        for dis in self:
            if dis.discount != 0.00:
                taxable_amount = dis.quantity * dis.price_unit
            else:
                taxable_amount = dis.price_subtotal
        return  '%.2f' % taxable_amount

    def tax_amount_line(self):
        tax_amount = 0.00
        for tax_amt in self:
            if tax_amt.discount != 0.00:
                account_tax = self.env['account.tax'].search([('name','=',tax_amt.tax_ids.name)])
                for tax in account_tax:
                    taxable_amount = tax_amt.quantity * tax_amt.price_unit
                    tax_amount = taxable_amount * (tax.amount/100)
            else:
                account_tax = self.env['account.tax'].search([('name','=',tax_amt.tax_ids.name)])
                for tax in account_tax:
                   tax_amount = tax_amt.price_subtotal * (tax.amount/100)
        return '%.2f' % tax_amount

    def total_taxable_amount_line(self):
        for tax_amt in self:
            if tax_amt.discount != 0.00:
                account_tax = self.env['account.tax'].search([('name', '=', tax_amt.tax_ids.name)])
                for tax in account_tax:
                    taxable_amount = tax_amt.quantity * tax_amt.price_unit
                    tax_amount = taxable_amount * (tax.amount / 100)
                    total_amount = taxable_amount + tax_amount
            else:
                account_tax = self.env['account.tax'].search([('name', '=', tax_amt.tax_ids.name)])
                for tax in account_tax:
                    tax_amount = tax_amt.price_subtotal * (tax.amount / 100)
                    total_amount = tax_amt.price_subtotal + tax_amount
        return  '%.2f' % total_amount





