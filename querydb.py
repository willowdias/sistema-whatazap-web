from os import error
import sqlite3
from sqlite3.dbapi2 import Cursor


class sqlite_db:
    def __init__(self,banco =None):
        self.conn =None
        self.curso = None
        if banco:
            self.open(banco)

    
    def open(self,banco):
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
            #print('acesso')
        except:
           print('invalido')       
    def creartabelas(self):
        cur = self.cursor
        cur.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome text NOT NULL, contato INTEGER, endereco text NOT NULL, cidade text NOT NULL,n INTEGER,cep INTEGER,email text NOT NULL);")
    def adicionar_apaga_incluir(self,query):
         cur = self.cursor
         cur.execute(query)
         self.conn.commit()
    def pega_dados(self,query):
        cur = self.cursor
        cur.execute(query)
        return cur.fetchall()
    
db = sqlite_db("banco_bd.db")

db.creartabelas()
#db.cadastro()
