from flask import Flask, jsonify, request

app = Flask(__name__)

projects = [
    {
        "id": 1,
        "title": "Projeto Brasa",
        "description": "Lorem ipsum",
        "images": [
            {
                "id": 1,
                "url": "https://www.google.com.br/iamgem.webp"
            },
                        {
                "id": 2,
                "url": "https://www.google.com.br/iamgem.webp"
            }

        ]
    }
]

# Consultar(todos)
@app.route('/',methods=['GET'])
def obter_livros():
    return jsonify(projects)

# Consultar(id)
@app.route('/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for project in projects:
        if project.get('id') == id:
            return jsonify(project)

app.run(port=5000,host='26.127.215.51',debug=True)





