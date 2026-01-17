app_name = "alphax_pos_suite"
app_title = "AlphaX POS Suite"
app_publisher = "AlphaX"
app_description = "Unified POS Suite for ERPNext (Restaurant/Cafe/Retail/Pharma)"
app_email = "support@example.com"
app_license = "MIT"

fixtures = [
    "Role",
    "Custom Field",
    "Property Setter",
]

doc_events = {
    "AlphaX POS Order": {
        "on_submit": "alphax_pos_suite.pos.posting.on_order_submit",
        "on_cancel": "alphax_pos_suite.pos.posting.on_order_cancel",
    }
}

scheduler_events = {
    "daily": [
        "alphax_pos_suite.pos.maintenance.daily_cleanup",
    ]
}
