import fastapi
import uvicorn
from typing import Optional

api = fastapi.FastAPI()


@api.get("/")
def index():
    body = (
        "<html>"
        "<body style='padding: 10px;'>"
        "<h1>Ciao PythonBiellaGroup</h1>"
        "</body>"
        "</html>"
    )
    # return {"message": body}
    return fastapi.responses.HTMLResponse(content=body)


@api.get("/default")
def default():
    """
    Torniamo un default
    """
    return {"messaggio": "PythonBiellaGroup!"}


@api.get("/api/test/{x}")
def calcola(x: int, y: int = 50, z: Optional[int] = None):
    if z == 0 or z is None:
        return fastapi.responses.JSONResponse(content={"Errore": "Z non è valorizzato"}, status_code=400)
    somma = x + y
    divisione = somma / z
    return {"x": x, "y": y, "z": z, "somma": somma, "divisione": divisione}


if __name__ == "__main__":
    uvicorn.run(api, port="8000", host="127.0.0.1")