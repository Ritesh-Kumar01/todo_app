from db import get_connection

def view_single_task(todoId):
    con = get_connection()
    cur = con.cursor()
    cur.execute("""SELECT * FROM todo WHERE todoID = ? """,(todoId,))
    row = cur.fetchone()
    con.close()
    return row

def view_task():
    con = get_connection()
    cur = con.cursor()
    cur.execute("""SELECT * FROM todo""")
    rows = cur.fetchall()
    con.close()
    return rows


def add_task(task_name,task_desc,status="Not Completed"):
    con = get_connection()
    cur = con.cursor()
    cur.execute("""
        INSERT INTO todo (todo_name, todo_desc, status)
        VALUES (?, ?, ?)
    """, (task_name, task_desc,status))
    con.commit()

def update_task(task_id, new_name, new_desc, new_status=0):
    con = get_connection()
    cur = con.cursor()
    if new_status == 1:
        status = "Completed"
    else:
        status = "Not Completed"

    cur.execute("""
        UPDATE todo
        SET todo_name = ?, todo_desc = ?, status = ?
        WHERE todoID = ?
    """, (new_name, new_desc, status, task_id))
    
    row =  cur.rowcount
    
    con.commit()
    con.close()
    return row


def delete_task(task_id):
    con = get_connection()
    cur = con.cursor()
    cur.execute("""DELETE FROM todo WHERE todoID = ?""",(task_id,))
    total_row = cur.rowcount
    con.commit()
    con.close()
    return total_row