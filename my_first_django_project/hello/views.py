from django.shortcuts import render

# Create your views here.

import textwrap

from django.http import HttpResponse
from django.views.generic.base import View

class HomePageView(View):
    def dispatch(request, *args, **kwargs): #what is kwargs#
        response_text = textwrap.dedent('''\
                                        <html>
                                        <head>
                                            <title> Hello World</title>
                                        </head>
                                        <body>
                                            <h1>Hello again</h1>
                                            <p> once again</p>
                                        </body>
                                        </html>
                                    ''')
        return HttpResponse(response_text)
