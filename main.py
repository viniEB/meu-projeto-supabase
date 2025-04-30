from fastapi import FastAPI
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASEURL")
SUPABASE_KEY = os.getenv("SUPABASEKEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API do Canil Municipal está online!"}

@app.get("/animais")
def listar_animais():
    resposta = supabase.table("animais").select("*").execute()
    return resposta.data

@app.post("/adotar")
def adotar_animal(animal_id: int, nome_adotante: str, contato: str):
    resultado = supabase.rpc("registrar_adocao", {
        "p_animal_id": animal_id,
        "p_nome_adotante": nome_adotante,
        "p_contato": contato
    }).execute()
    return {"resultado": resultado.data}
