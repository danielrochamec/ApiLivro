from flask import Flask, jsonify, request

app = Flask(__name__)

livros =[
    {
        'id': 1,
        'título': 'O Senhor dos Anéis - A Sociedade do Anel ',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'O Senhor dos Anéis - As Duas Torres ',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 3,
        'título': 'O Senhor dos Anéis - O Retorno do Rei ',
        'autor': 'J.R.R Tolkien'
    }
]
#Consultar
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#CONSULTAR ID
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
#EDITAR LIVROS    
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
#CRIAR
@app.route('/livros', methods=['POST'])
def incluir_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)
    
#EXCLUIR
@app.route('/livros/<int:id>', methods=["DELETE"])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)


    #RUN DO APP.
app.run(port=5000,host='localhost',debug=True)