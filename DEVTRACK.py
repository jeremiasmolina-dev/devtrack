import mysql.connector
from datetime import date

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="NAME",        
        password="PASSWORD", 
        database="devtrack"
    )
    return conn

def menudev():
    print("[1] Cursos")
    print("[2] Proyectos")
    print("[3] Objetivos")
    print("[4] Salir")


def menu_Cursos(cursor, conn):
    print("\n [Cursos]")
    print("[1] Ver todos los cursos")
    print("[2] Actualizar progreso/estado")
    print("[3] Agregar un curso nuevo")
    sub = input("Opcion: ")

    if sub == "1":
            cursor.execute("SELECT id, nombre, progreso, fecha_inicio, estado FROM cursos;")
            for row in cursor.fetchall(): 
                 print(row)
    elif sub == "2":
         id_curso = input("ID del curso a actualizar: ")
         progreso_curso = input("Nuevo Progreso [0/100]: ")
         estado_curso = input("Nuevo estado [no iniciado/en progreso/completado]: ")
         cursor.execute(
              "UPDATE cursos SET progreso=%s, estado=%s WHERE id=%s",
              (progreso_curso, estado_curso, id_curso)
         )
         conn.commit() 
         print("Curso Actualizado.")         

    elif sub == "3":
         nombre_curso = input("Ingrese el nombre del nuevo curso: ")
         fecha_inicio = date.today()

         cursor.execute(
              "INSERT INTO cursos (nombre, progreso, fecha_inicio, estado) VALUES (%s, %s, %s, %s)",
              (nombre_curso, "0", fecha_inicio, "No iniciado")
              )
         conn.commit()
         print("Curso agregado de nazi")

def menu_proyectos(cursor, conn):
    print("\n [Proyectos]")
    print("[1] Ver todos")
    print("[2] Actualizar")
    print("[3] Agregar proyecto")
    sub = input("Selecciona una opción: ")
    if sub == "1":
     cursor.execute(
          "SELECT id, nombre, descripcion, fecha_inicio, lenguaje, estado FROM proyectos"
     )
     for row in cursor.fetchall():
          print(row)

    elif sub == "2":
     id_proy = input("ID del proyecto a actualizar: ")
     progreso_proy = input("Progreso nuevo [0/100]: ")
     estado_proy = input("Nuevo estado [No iniciado/en progreso/finalizado]: ")
     cursor.execute(
          "UPDATE proyectos SET progreso=%s, estado=%s WHERE id=%s",
          (progreso_proy, estado_proy, id_proy)
     )
     conn.commit()
     print("Proyecto actualizado.")

    elif sub == "3":
        nombre_curso = input("Ingrese el nombre del nuevo curso: ")
        fecha_inicio = date.today()
        cursor.execute(
         "INSERT INTO proyectos (nombre, progreso, fecha_inicio, estado) VALUES (%s, %s, %s, %s)",
         (nombre_curso, "0", fecha_inicio, "No iniciado")
         )
        conn.commit()
        print("Curso agregado de nazi")


def menu_objetivos(cursor, conn):
    print("\n [Objetivos]")
    print("[1] Ver todos")
    print("[2] Actualizar")
    print("[3] Agregar objetivo")
    sub = input("Selecciona una opción: ")

    if sub == "1":
        cursor.execute(
            "SELECT id, nombre, descripcion, progreso, estado FROM objetivos;"
        )
        for row in cursor.fetchall():
            print(row)

    elif sub == "2":
        id_obj = input("ID del objetivo a actualizar: ")
        progreso_obj = input("Nuevo Progreso [0-100]: ")
        estado_obj = input("Nuevo estado [No iniciado/en progreso/finalizado]: ")
        cursor.execute(
            "UPDATE objetivos SET progreso=%s, estado=%s WHERE id=%s",
            (progreso_obj, estado_obj, id_obj)
        )
        conn.commit()
        print("Objetivo actualizado.")
    elif sub == "3":
        nombre_obj = input("Ingrese el nombre del nuevo objetivo: ")
        descripcion = input("Descripcion del objetivo: ")
        cursor.execute(
          "INSERT into objetivos (nombre, descripcion, progreso, estado) VALUES (%s, %s, %s, %s)",
          (nombre_obj, descripcion, 0, "No iniciado") 
          )
        conn.commit()
        print("Objetivo nuevo creado correctamente.")

# MAIN -------

conn = connect_db()
cursor = conn.cursor()

menudev()
option = int(input("Ingresa la opción:"))

while option != 4:
    if option == 1:
        menu_Cursos(cursor, conn)
    elif option == 2:
        menu_proyectos(cursor, conn)
    elif option == 3:
        menu_objetivos(cursor, conn)
    else:
        print("No es una opcion valida")
    menudev()
    option = int(input("Ingresa la opción:"))

conn.close()
print("Tarea finalizada.")
