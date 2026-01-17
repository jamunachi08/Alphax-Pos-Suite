import frappe
from frappe.model.document import Document
from alphax_pos_suite.pos.shift import get_shift_expected_cash

class AlphaXPOSShift(Document):
    def before_insert(self):
        if not self.opened_on:
            self.opened_on = frappe.utils.now_datetime()

    def validate(self):
        if self.status == "Closed":
            self.expected_cash = get_shift_expected_cash(self.name)
            self.variance = (self.closing_cash or 0) - (self.expected_cash or 0)
