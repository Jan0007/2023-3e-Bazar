from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

def index(request):
    """ - TODO fix this shit
    #opens connection
    connection = psycopg2.connect(user="postgres",
                                  password="Kiblicek009",
                                  host="localhost",
                                  port="5432",
                                  database="postgres")
    cursor = connection.cursor()
    connection.autocommit = True

    #inserts
    cursor.execute('''INSERT INTO users_constrained (id, mail, password, username) VALUES ('example@lol.com', 'Kokot', 'Karel')''')
    
    #closes connection
    connection.commit()
    print('commited')
    """
    return render(request, 'homepage.html')