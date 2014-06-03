from flask import Flask
from flask.ext.admin import Admin, BaseView, expose

app = Flask(__name__)


class AdminTestView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')


admin = Admin(app)
admin.add_view(AdminTestView(name='AdminTest'))

app.run(debug=True)