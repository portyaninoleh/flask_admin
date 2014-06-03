from flask import Flask
from flask.ext.admin import Admin, BaseView, expose

app = Flask(__name__)


class AdminTestView(BaseView):
    def is_accessible(self):
        return login.current_user.
    @expose('/')
    def index(self):
        return self.render('index.html')


admin = Admin(app)
admin.add_view(AdminTestView(name='Item1', endpoint='item1', category='DropDown'))
admin.add_view(AdminTestView(name='Item2', endpoint='item2', category='DropDown'))
admin.add_view(AdminTestView(name='Item3', endpoint='item3', category='DropDown'))

app.run(debug=True)