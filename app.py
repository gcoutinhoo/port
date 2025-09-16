from flask import Flask, render_template
import requests

app = Flask(__name__)

GITHUB_USERNAME = "gcoutinhoo"
PROJETOS_DESTAQUE = ["Jornada-Python", "Projeto-RAD"]

def get_repos():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    response = requests.get(url)
    
    if response.status_code == 200:
        repos = response.json()
        projetos = []
        for repo in repos:
            if repo["name"] in PROJETOS_DESTAQUE:
                projetos.append({
                    "nome": repo["name"],
                    "descricao": repo["description"],
                    "linguagem": repo["language"],
                    "url": repo["html_url"]
                })
        return projetos
    else:
        print(f"Erro ao acessar a API do GitHub: {response.status_code}")
        return []

@app.route("/")
def index():
    projetos = get_repos()
    return render_template("index.html", projetos=projetos, github=GITHUB_USERNAME)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
