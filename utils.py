import json
from urllib.parse import unquote_plus

def extract_route(request):
    req = request.split('\n')
    for line in req:
        if 'GET' in line or 'POST' in line:
            split = line.split(' ')
            string = split[1]
        return string[1:]


def read_file(file):
    cd = file.suffix
    if cd == ".js" or cd == ".txt" or cd == ".html" or cd == ".css":
        with open(file, 'r', encoding='utf-8') as f:
            read = f.read().encode()
    else:
        with open(file, 'rb') as p:
            read = p.read()
    return read


def load_data(db):
    #print(db.get_all())
    return db.get_all()


# def salva_param(request):
#     request = request.replace('\r', '') 
#     partes = request.split('\n\n')
#     partes_1 = partes[1]
#     corpo = unquote_plus(partes_1) 
#     params = {}
#     for chave_valor in corpo.split('&'):
#         values = chave_valor.split('=')
#         if chave_valor.startswith('titulo'):
#             params['titulo'] = values[1]
#         elif chave_valor.startswith('detalhes'):
#             params['detalhes'] = values[1]


def load_template(file):
    caminho = "templates/" + file
    with open(caminho, 'r') as f:
        read = f.read()
    return read


# PEGUEI DESSE LINK https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages
def build_response(body='', code=200, reason='OK', headers=''):
    status_line = 'HTTP/1.1 '+ str(code) + ' ' + reason
    if headers != '':
        headers = '\n'+headers
    
    if isinstance(body, str):
        body = body.encode()
    response = (status_line + headers + '\n\n').encode() + body 
    return response