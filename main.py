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

@app.post("/habitos")
def criar_habito(habito: Habito):
    global contador_id
    habito.id = contador_id
    contador_id += 1
    habitos_db.append(habito)
    return habito

from fastapi import FastAPI, HTTPException
@app.delete("/habitos/{habito_id}")
def deletar_habito(habito_id: int):
    for i, h in enumerate(habitos_db):
        if h.id == habito_id:
            habitos_db.pop(i)
            return {"mensagem": "Habito deletado com sucesso"}
    raise HTTPException(status_code=404, detail="Hábito não encontrado")
