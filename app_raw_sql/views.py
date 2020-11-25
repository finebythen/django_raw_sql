from django.shortcuts import render
from django.db import connections, transaction

from .models import Person


def main(request):
    # standard database-query
    standard_query = Person.objects.all()

    # raw-sql database-query
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute("SELECT * FROM app_raw_sql_person")
            row = cursor.fetchall()
    except Exception as e:
        cursor.close()

    try:
        with connections['default'].cursor() as cursor:
            cursor.execute("SELECT * FROM app_raw_sql_person WHERE last_name='Doe'")
            row = cursor.fetchall()
    except Exception as e:
        cursor.close()

    try:
        with connections['default'].cursor() as cursor:
            cursor.execute("UPDATE app_raw_sql_person SET age=20 WHERE first_name='Jane'")
    except Exception as e:
        cursor.close()

    context = {'standard_query': standard_query}
    return render(request, 'app_raw_sql/main.html', context)
