###Шаблон MVC (Model-View-Controller):
# Модель (Model)
class User:
    def __init__(self, name):
        self.name = name

# Представление (View)
class UserView:
    def display_user_details(self, user):
        print(f"User: {user.name}")

# Контроллер (Controller)
class UserController:
    def __init__(self, user, view):
        self.user = user
        self.view = view

    def update_user_name(self, new_name):
        self.user.name = new_name
        self.view.display_user_details(self.user)

# Использование
user = User("Alexander")
view = UserView()
controller = UserController(user, view)
controller.update_user_name("Kate")


###Шаблон MVVM (Model-View-ViewModel):
# Модель (Model)
class User:
    def __init__(self, name):
        self.name = name

# Представление (View)
class UserView:
    def display_user_details(self, user):
        print(f"User: {user.name}")

# ViewModel
class UserViewModel:
    def __init__(self, user):
        self.user = user

    def update_user_name(self, new_name):
        self.user.name = new_name

    def display_user_details(self, view):
        view.display_user_details(self.user)

# Использование
user = User("Sergey")
view = UserView()
view_model = UserViewModel(user)

view_model.display_user_details(view)
view_model.update_user_name("Alina")
view_model.display_user_details(view)


###Шаблон MVP (Model-View-Presenter):
# Модель (Model)
class User:
    def __init__(self, name):
        self.name = name

# Представление (View)
class UserView:
    def display_user_details(self, user):
        print(f"User: {user.name}")

# Презентер (Presenter)
class UserPresenter:
    def __init__(self, user, view):
        self.user = user
        self.view = view

    def update_user_name(self, new_name):
        self.user.name = new_name
        self.view.display_user_details(self.user)

# Использование
user = User("Anton")
view = UserView()
presenter = UserPresenter(user, view)
presenter.update_user_name("Dasha")