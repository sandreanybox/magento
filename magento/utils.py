# -*- coding: UTF-8 -*-
'''
    magento.utils

    General purpose utility functions

    :copyright: (c) 2010 by Sharoon Thomas.
    :copyright: (c) 2010 by Openlabs Technologies & Consulting (P) LTD.
    :license: AGPLv3, see LICENSE for more details
'''

def expand_url(url, protocol, xdebug=None):
    """
    Expands the given URL to a full URL by adding
    the magento soap/wsdl parts

    :param url: URL to be expanded
    :param service: 'xmlrpc' or 'soap'
    """
    if protocol == 'soap':
        ws_part = 'api/?wsdl'
    else:
        ws_part = 'index.php/api/xmlrpc'
    if xdebug is not None:
        ws_part += '?XDEBUG_SESSION_START=ECLIPSE_DBGP&KEY=' + xdebug
    return url.endswith('/') and url + ws_part or url + '/' + ws_part
