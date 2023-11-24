from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
import json
import uvicorn


app = FastAPI()

def generar_instalaciones(data):
    table_html = "<table border='1'><tr><th>Tipo de Instalación</th><th>Cantidad</th></tr>"

    instalaciones = data['data']['Total']['Instalaciones']
    for tipo_instalacion, count in instalaciones.items():
        if tipo_instalacion != 'Total':
            table_html += f"<tr><td>{tipo_instalacion}</td><td>{count}</td></tr>"

    table_html += "</table>"
    return table_html

def generar_piscinas_cubiertas(data):
    table_html = "<table border='1'><tr><th>Municipio</th><th>Cantidad</th></tr>"

    piscina_cubierta = data['data']['Piscina cubierta']['Instalaciones']
    for municipio, count in piscina_cubierta.items():
        if municipio != 'Total':
            table_html += f"<tr><td>{municipio}</td><td>{count}</td></tr>"

    table_html += "</table>"
    return table_html


def generar_pistas_estadistica_comparacion(data):
    table_html = "<table border='1'><tr><th>Tipo de Instalación</th><th>Cantidad</th></tr>"

    pistas_cubiertas = data['data']['Pista polideportiva cubierta']['Instalaciones']['Total']
    pistas_descubiertas = data['data']['Pista polideportiva descubierta']['Instalaciones']['Total']

    table_html += f"<tr><td>Pistas Deportivas Cubiertas</td><td>{pistas_cubiertas}</td></tr>"
    table_html += f"<tr><td>Pistas Deportivas Descubiertas</td><td>{pistas_descubiertas}</td></tr>"

    table_html += "</table>"
    return table_html





#-----
@app.get("/instalaciones", response_class=HTMLResponse)
async def get_instalaciones(request: Request):
    with open('Instalaciones_deportivas.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        table_html = generar_instalaciones(data)
        return HTMLResponse(content=f"""
            <html>
                <head>
                    <title>Instalaciones Deportivas</title>
                </head>
                <body>
                    {table_html}
                </body>
            </html>
        """)
        
        

@app.get("/piscinas_cubiertas", response_class=HTMLResponse)
async def get_piscinas(request: Request):
    with open('Instalaciones_deportivas.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        table_html = generar_piscinas_cubiertas(data)
        return HTMLResponse(content=f"""
            <html>
                <head>
                    <title>Instalaciones Deportivas</title>
                </head>
                <body>
                    {table_html}
                </body>
            </html>
        """)
        
        
@app.get("/comparacion_pistas", response_class=HTMLResponse)
async def get_pistas(request: Request):
    with open('Instalaciones_deportivas.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        table_html = generar_pistas_estadistica_comparacion(data)
        return HTMLResponse(content=f"""
            <html>
                <head>
                    <title>Instalaciones Deportivas</title>
                </head>
                <body>
                    {table_html}
                </body>
            </html>
        """)
        
        
    
@app.get("/", response_class=HTMLResponse)
async def get_pistas(request: Request):
    return FileResponse("static/cliente.html")
        


             
        
print()
if __name__ == "__main__":
    print("-> Inicio integrado de servicio web")
    uvicorn.run(app, host="127.0.0.1", port=800)
    #cambiado el puerto...
else:
    print("=> Iniciado desde el servidor web")
    print("   Módulo python iniciado:", __name__)
