import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\stud\Documents\123.accdb;'
    conn = pyodbc.connect(con_string)

    Выставки_id = 2

    cur = conn.cursor()
    cur.execute('DELETE FROM Выставки WHERE id = ?', (Выставки_id))
    conn.commit()
    print("Data Deleted ")

except pyodbc.Error as e:
    print("Error in Connection")
