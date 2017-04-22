from bottle import run, route, error, template, abort, request, response
from quotes import choose_quote, choose_quote_by_id
from  login import check_login
import logging


# Настройка логера
logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG)


# Создание собственной страницы ошибки
@error(404)
def error_404(error):
    return '<h1>Запрошенная Вами страница не существует или переименована, ' \
           'или черт его знает, где теперь находится.</h1>'


# Статический роутинг
@route('/')
def index():
    dict_quote = choose_quote()
    return template('index', id=dict_quote['id'], phrase=dict_quote['phrase'], signature=dict_quote['signature'])


# Динамический роутинг
@route('/<id:int>')
def json_quote(id):

    json_data = choose_quote_by_id(id)
    if json_data is not None:
        return json_data
    else:
        return abort(404)


# Это пример использования разных методов в роутинге для логина и пример куки
@route('/login')
def login():
    if request.get_cookie("visited"):
        return "Рады видеть вас снова, не хотите <a href=/>цитату</a>?</p>"
    else:
        response.set_cookie("visited", "yes")
        return '''
        <form action="/login" method="post">
            Имя пользователя: <input name="username" type="text" />
            Пароль: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


@route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Добро пожаловать {}, не хотите <a href=/>цитату</a>?</p>".format(username)
    else:
        return "<p>Неверные данные.</p>"


if __name__ == '__main__':
    run(debug=True, reloader=True)
