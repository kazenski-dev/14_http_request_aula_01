from http import HTTPStatus
from __init__ import app


@app.route("/") # mapear o recurso
def contexto_app():
    #retorno uma string que quero apresentar na tela
    return "Bem vindo ao CRUD de estudante 21:14", HTTPStatus.OK

@app.route("/estudante", methods=['POST']) #post para cadastrar
def salvar():
    return "Criando usuario de estudante", HTTPStatus.CREATED

@app.route("/pessoa", methods=['GET']) #get sempre listagem
def listar_todos():
    return "Voce esta listando pessoas", HTTPStatus.OK

@app.route("/pessoa/<id>", methods=['GET']) #get sempre listagem
def listar_by_id(id):
   return "listando pelo id" + str(id), HTTPStatus.OK

@app.route("/pessoa/<id>", methods=['DELETE'])
def excluir(id):
    return "Registro excluido com sucesso", HTTPStatus.OK

@app.route("/pessoa/<id>", methods=['PUT']) #update
def editar(id):
   return "editando pelo id" + str(id), HTTPStatus.OK

if __name__ == "__main__":
    app.run(debug=True)