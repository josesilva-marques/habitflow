from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Habito(BaseModel):
    id: int = 0
    nome: str
    descricao: str = ""

habitos_db: List[Habito] = []
contador_id = 1

@app.get("/")
def root():
    """Endpoint principal da API."""
    return {"mensagem": "HabitFlow API funcionando!"}

@app.get("/habitos")
def listar_habitos():
    return habitos_db

@app.post("/habitos", response_model=Habito)
def criar_habito(habito: Habito):
    global contador_id
    novo = Habito(id=contador_id, nome=habito.nome, descricao=habito.descricao)
    habitos_db.append(novo)
    contador_id += 1
    return novo

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
