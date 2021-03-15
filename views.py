from utils import load_data, load_template, build_response
from database import Note, Database
import urllib.parse
#from gevent.testing import params

def index(request, db):
    
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '') 
        partes = request.split('\n\n')
        partes_1 = partes[1]
        params = {}

        if "id" in partes_1:
            idd = partes_1[3:]
            db.delete(idd)
        
        else:
            for chave_valor in partes_1.split('&'):
                chave_valor = urllib.parse.unquote_plus(chave_valor)
                separado = chave_valor.split('=')
                params[separado[0]] = separado[1]

            note = Note()
            note.title = params['titulo']
            note.content = params['detalhes'] 

            if 'update' in params.keys():
                note.id = params['update']
                db.update(note)
            
            elif 'delete' in params.keys():
                db.delete(params['delete'])

            else:
                db.add(note)
            
            return build_response(code=303, reason='See Other', headers='Location: /')

        #UPDATE

        # if partes_1.startswith('id'):
        #     idzao = partes_1[:3] #corta o id:
        #     db.delete(idzao)
        # elif partes_1.startswith('update'):
        #     notao = {}
        #     for chave_valor in partes_1.split('&'):
        #         if 'titulo' in chave_valor:
        #             titulo = urllib.parse.unquote_plus(chave_valor[7:])
        #             titulo = notao['title']

        #         elif 'id' in chave_valor:
        #             ide = chave_valor[3:]
        #             ide = notao['id']

        #         elif 'detalhes' in chave_valor:
        #             det = urllib.parse.unquote_plus(titulo)
        #             det = notao['content']

        #     db.update(titulo, det, ide)

        # #ADD

        # else:
        #     for chave_valor in partes_1.split('&'):
        #         if 'titulo' in chave_valor:
        #             titulo = urllib.parse.unquote_plus(chave_valor[7:])
        #             titulo = params['titulo']

        #         elif 'detalhes' in chave_valor:
        #             detao = urllib.parse.unquote_plus(chave_valor[9:])
        #             detao = params['detalhes']
        
        # note = db.add(Note(title = params[titulo], content= params['detalhes']))


        #note = Note(title = params[titulo], content = params['detalhes'])


    # O RESTO DO CÓDIGO DA FUNÇÃO index CONTINUA DAQUI PARA BAIXO..
    #else:
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados.title, details=dados.content, id = dados.id)
        for dados in load_data(db)
    ]
    notes = '\n'.join(notes_li)

    return build_response(load_template('index.html').format(notes=notes))
