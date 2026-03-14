from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Habito(BaseModel):
    id: int
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
