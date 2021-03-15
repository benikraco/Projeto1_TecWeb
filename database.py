import sqlite3

tabela = "CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title STRING, content STRING NOT NULL)"
inserir = "INSERT INTO note (id, title, content) VALUES ("

from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self, banco):
        banco = banco + ".db"
        self.conn = sqlite3.connect(banco)
        note = self.conn.execute(tabela)
    
    def add (self, note):
        toExec ="INSERT INTO note (title, content) VALUES ('{}', '{}')".format(note.title, note.content)
        print (toExec)
        self.conn.execute(toExec)
        self.conn.commit()
 
    def get_all (self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        print (cursor)
        lista = []
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            note = Note(id,title,content)
            lista.append(note)
        return lista

    def update (self, entry):
        receb = "UPDATE note SET title = '{0}', content = '{1}' WHERE id = {2}".format(entry.title, entry.content, entry.id)
        self.conn.execute(receb)
        self.conn.commit()
    
    def delete(self, note_id):
        receive = "DELETE FROM note WHERE id = {0}".format(note_id)
        self.conn.execute(receive)
        self.conn.commit()