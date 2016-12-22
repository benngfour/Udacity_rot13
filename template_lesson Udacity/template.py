import os

import jinja2
import webapp2
import string
from string import maketrans

template_dir = os.path.join(os.path.dirname(__file__), 'template')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape = True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        items = self.request.get_all("food")
        self.render("shopping_list.html", items = items)

class FizzBuzzHandler(Handler):
    def get(self):
        n = self.request.get('n', 0)
        n = n and int(n)
        self.render('fizzbuzz.html', n = n)

#class Rot13Handler(Handler):
#    def rot13(self, text):
#        textin = "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz"
#        textout = "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
#        textrot13 = maketrans(textin, textout)
#        newtext = text.translate(textrot13)
#        return newtext
#
#    def get(self):
#        self.render("rot13.html")
#
#    def post(self):
#        text = self.request.get("newtext")
#        self.render("rot13.html", text = text)

class Rot13Handler(Handler):

    def get(self):

        self.render('rot13.html')


    def post(self):

        rot13 = ''

        text = self.request.get('text')

        if text:
            rot13 = text.encode('rot13')
        self.render('rot13.html', text=rot13)

app = webapp2.WSGIApplication([('/', MainPage),
                                ('/fizzbuzz', FizzBuzzHandler),
                                ('/rot13', Rot13Handler)
                              ],
                              debug=True)
