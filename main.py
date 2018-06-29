from tkinter import *
from tkinter import ttk
import sqlite3

con = sqlite3.connect('database.db')
c = con.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS Dados(nome text,numero text)
""")


def read():
    for clear in treeview.get_children():
        treeview.delete(clear)
    c.execute("""
    SELECT * FROM Dados
    """)
    dados = ''
    for dados in c.fetchall():
        treeview.insert("", 0, text=dados[0], values=dados[1])

def create():
    name = et_name.get()
    num = et_num.get()
    if (name, num) == ('', ''):
        lb_result['text'] = 'Prencha todos os Campos'
        lb_result['fg'] = 'red'
    else:
        if num == '':
            lb_result['text'] = 'Prencha todos o Numero'
            lb_result['fg'] = 'red'
        else:
            treeview.insert("", 0, text=name, values=num)
            c.execute("""
            INSERT INTO Dados(nome, numero) VALUES(?,?)
            """, (name, num))
            con.commit()



def update():
    name = et_name.get()
    num = et_num.get()
#    et_name.delete(0, END)
#    et_num.delete(0, END)
#    sql = 'SELECT * FROM Dados WHERE nome = ?'
#    for row in c.execute(sql, (name,)):
#        old = row
    c.execute("""
    UPDATE Dados
    SET nome = ?, numero = ?""", ('Teste', '000',))
    con.commit()

def delete():
    pass


def tree(event):
    for item in treeview.selection():
        item_text = treeview.item(item, "text")
    sql = 'SELECT * FROM Dados WHERE nome = ?'
    for rst in c.execute(sql, (item_text,)):
        lb_result['text'] = 'Nome: "{}" Numero: "{}"'.format(rst[0], rst[1])
        lb_result['fg'] = 'black'



tk = Tk()
tk.title("My First Crud")
edit = LabelFrame(tk, text='Editar')
gui = LabelFrame(tk, text='Pesquisa')
gui.grid(row=0, column=0)
edit.grid(row=1, column=0, sticky=W+E)
lb_pesq = Label(gui, text='Pesquisar: ').grid(row=0, column=0, sticky=E)
et_pesq = Entry(gui).grid(row=0, column=1, sticky=W+E)
bt_pesq = Button(gui, text='Pesquisar', command=read).grid(row=0, column=2, sticky=W+E)
lb_result = Label(gui, text='')
lb_result.grid(row=1, columnspan=3)
treeview = ttk.Treeview(gui, columns="#0")
scrolbar = ttk.Scrollbar(gui)
treeview.heading(column="#0", text="Nome")
treeview.heading(column="#1", text="Numero")
treeview.bind("<<TreeviewSelect>>", tree)
scrolbar.grid(row=2, column=4, sticky=N+S)
read()
treeview.grid(row=2, columnspan=3, sticky=W+E)

lb_name = Label(edit, text='Nome: ').grid(row=3, column=0, sticky=W)
lb_num = Label(edit, text='Numero: ').grid(row=3, column=1, sticky=W)
et_name = Entry(edit)
et_name.grid(row=4, column=0)
et_num = Entry(edit)
et_num.grid(row=4, column=1)
bt_create = Button(edit, text='Cadastrar', bg='green', fg='black', command=create).grid(row=5, column=0, sticky=W+E)
bt_edit = Button(edit, text='Editar', bg='orange', fg='black', command=update).grid(row=5, column=1, sticky=W+E)
bt_delet = Button(edit, text='Deletar', bg='red', fg='black', command=delete).grid(row=5, column=2, sticky=W+E)
gui.mainloop()

#        treeview.insert("", 0, text="NOME", values=("NUMERO"))

"""
    global row
    row = None
    name = et_name.get()
    num = et_num.get()
    if (name, num) == ('', ''):
        lb_result['text'] = "Preencher o formulario"
        lb_result['fg'] = 'red'
    else:
        if num == '':
            lb_result['text'] = "Preencher o Numero"
            lb_result['fg'] = 'red'
        else:
            if read() == None:
                lb_result['text'] = "Cadastrado com Sucesso!"
                lb_result['fg'] = 'green'
                c.execute("INSERT INTO Dados(nome, numero) VALUES(?,?)", (name, num))
                con.commit()
                treeview.insert("", 0, text=name, values=num)
                et_name.delete(0, END)
                et_num.delete(0, END)
            else:
                sql = 'SELECT * FROM Dados WHERE nome = ?'
                for row in c.execute(sql, (name,)):
                    print(row[0])
                if row[0] == name:
                    lb_result['text'] = "Ja Cadastrado!"
                    lb_result['fg'] = 'red'
                else:
                    lb_result['text'] = "Cadastrado com Sucesso!"
                    lb_result['fg'] = 'green'
                    c.execute("INSERT INTO Dados(nome, numero) VALUES(?,?)", (name, num))
                    con.commit()
                    treeview.insert("", 0, text=name, values=num)
                    et_name.delete(0, END)
                    et_num.delete(0, END)

"""












