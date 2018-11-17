import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')  # templates directory added in our current dir.
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

form_html = """
<form>
<h2>Add a food</h2>
<input type="text" name="food">
%s
<button>Add</button>
</form>
"""

hidden_html = """
<input type="hidden" name="food" value="%s">
"""

item_html = """
<li>
%s
</li>
"""

shopping_list_html = """
<br>
<br>
<h2>Shopping list</h2>
<ul>
%s
</ul
"""

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
        n = self.request.get('n')
        self.response.out.write(n)
        if n and n.isdigit():
            n = int(n)

        self.render("shopping_list.html", n=n)
        self.response.out.write(n)
        # output = form_html
        # output_hidden = ""
        #
        # items = self.request.get_all("food")  # list of all the food parameters
        # output_items = ""
        # if items:
        #     for item in items:
        #         output_hidden += hidden_html % item
        #         output_items += item_html % item
        #
        #     output_shopping = shopping_list_html % output_items
        #     output += output_shopping
        #
        # output = output % output_hidden
        #
        # self.write(output)


app = webapp2.WSGIApplication([('/', MainPage), ], debug=True)