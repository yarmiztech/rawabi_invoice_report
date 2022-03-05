{
    'name': "Inherit Rawabi E-Invoice ",
    'author':
        'ENZAPPS',
    'summary': """
This module is for Inheriting Rawabi Invoice Format.
""",

    'description': """
        This module is for Inheriting Rawabi Invoice Format.
    """,
    'website': "",
    'category': 'base',
    'version': '14.0',
    'depends': ['base','account','rawabi_invoice'],
    "images": ['static/description/icon.png'],
    'data': [
        'views/inherit_rawabi_invoice.xml',

    ],
    'demo': [
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
}
