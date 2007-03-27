# -*- coding: iso-8859-1 -*-
"""
    MoinMoin - logout action

    The real logout is done in MoinMoin.request.
    Here is just some stuff to notify the user.

    @copyright: 2005-2006 Radomirs Cirskis <nad2000@gmail.com>
    @license: GNU GPL, see COPYING for details.
"""

from MoinMoin.Page import Page

def execute(pagename, request):
    return LogoutHandler(pagename, request).handle()

class LogoutHandler:
    def __init__(self, pagename, request):
        self.request = request
        self._ = request.getText
        self.page = Page(request, pagename)

    def handle(self):
        _ = self._
        message = _("You are now logged out.")
        return self.page.send_page(msg=message)

