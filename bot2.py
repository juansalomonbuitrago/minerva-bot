from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Chatbot Minerva")

# Modelo de solicitud
class ChatRequest(BaseModel):
    opcion: int

@app.get("/")
def bienvenida():
    return {
        "mensaje": (
            "¡Hola! Soy el agente del Centro de Formación Minerva. Estoy aquí para ayudarte. "
            "Elige una opción:\n"
            "1. Información general\n"
            "2. Sociosanitario\n"
            "3. Administrativo\n"
            "4. Auxiliar enfermería\n"
            "5. Cajero reponedor"
        )
    }

@app.post("/chatbot")
def chatbot(request: ChatRequest):
    opciones = {
        1: "https://www.formacionminerva.com/cursos/",
        2: "https://www.formacionminerva.com/wp-content/uploads/2025/05/Catalogo-de-ATENCION-SOCIOSANITARIA-A-PERSONAS-DEPENDIENTES-EN-INSTITUCIONES-SOCIALES-.pdf",
        3: "https://www.formacionminerva.com/wp-content/uploads/2025/05/Catalogo-de-Auxiliar-administrativo-2.pdf",
        4: "https://www.formacionminerva.com/wp-content/uploads/2024/12/CATALOGO-NUEVO-CURSO-AUXILIAR-DE-ENFERMERIA-1-1.pdf",
        5: "https://www.formacionminerva.com/wp-content/uploads/2025/05/Catalogo-de-Cajero-Reponedor-.pdf"
    }

    if request.opcion not in opciones:
        return {"error": "Opción no válida. Por favor, elige un número del 1 al 5."}

    mensajes = {
        1: "Aquí tienes la información general de nuestros cursos:",
        2: "Consulta el catálogo de formación sociosanitaria aquí:",
        3: "Aquí puedes ver el catálogo del área administrativa:",
        4: "Accede al catálogo de cursos de auxiliar de enfermería:",
        5: "Consulta la formación disponible para cajero reponedor:"
    }

    return {
        "respuesta": mensajes[request.opcion],
        "enlace": opciones[request.opcion]
    }
