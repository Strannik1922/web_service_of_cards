# web_service_of_cards
Tree menu in Django

## Приложение для отрисовки меню с помощью templatetag

### Краткое описание:
Простое Django приложение для отрисовки древовидного меню, реализованное через templatetag. Меню и его элементы создаются и редактируются в админ панели Django. С помощью тега {% draw_menu 'menu_name' %} меню можно расположить на любой странице приложения.

### Requirements:
+ Django==2.2.16
+ pytz==2020.1
+ sqlparse==0.3.1

### Сборка и запуск:
! Для корректного отображения меню при запуске следует сначала создать его а так-же добавить в него элементы в админ панели Django.
```
git clone git@github.com:Strannik1922/web_service_of_cards.git
cd web_service_of_cards
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
