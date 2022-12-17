import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\stud\Documents\123.accdb;'
    conn = pyodbc.connect(con_string)
    print("Connected To Database")
    cursor  = conn.cursor()
    Выставки =(
        (14, 'Фантазия в нитях2', 'Николаевский зал', '07.12.2020', '08.12.2020', '5'),
        (15, 'Фантазия в нитях3', 'Николаевский зал', '07.12.2020', '08.12.2020', '5'),
        (16, 'Фантазия в нитях4', 'Николаевский зал', '07.12.2020', '08.12.2020', '5'),

    )

    cursor.executemany('INSERT INTO Выставки VALUES (?,?,?,?,?,?)', Выставки)
    conn.commit()
    print('Data Inserted')

except pyodbc.Error as e:
    print("Error in Connection", e)
