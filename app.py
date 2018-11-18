import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')  # templates directory added in our current dir.
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render(self, template, **kw):  # **kw are extra parameters
        self.response.out.write(self.render_str(template, **kw))

    def render_str(self, template, **params):  # **params are also extra parameters
        t = jinja_env.get_template(template)
        return t.render(params)

class MainPage(Handler):
        def get(self):
            items = self.request.get_all("food")  # will get all the parameters in url
            self.render("shopping_list.html", items=items)


class FizzBUzzHandler(Handler):
    def get(self):
        n = self.request.get('n', 0)
        if n:
            n = int(n)
        self.render('fizzbuzz.html', n=n)


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/fizzbuzz', FizzBUzzHandler)], debug=True)