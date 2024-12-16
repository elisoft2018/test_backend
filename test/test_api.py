import requests
import jsonschema
from jsonschema import validate

#Asignamos la API a la variable URL
url = 'https://fake-json-api.mock.beeceptor.com/companies'

#Establecemos la estructura esperada del JSON que retorna el API
expected_schema = {
    "type": "object",
    "properties": {
        "identificación": {"type": "integer"},
        "nombre": {"type": "string"},
        "dirección": {"type": "string"},
        "código postal": {"type": "string"},
        "país": {"type": "string"},
        "número de empleados": {"type": "integer"},
        "industria": {"type": "string"},
        "capitalización de mercado": {"type": "integer"},
        "dominio": {"type": "string"},
        "logotipo": {"type": "string"},
        "nombre del director ejecutivo": {"type": "string"}
    }
}


def test_response_status_code() -> None:
    #Realizamos la petición al API
    response = requests.get(url)

    status_code = response.status_code

    #Validamos el código de respuest
    assert (status_code ==200), f"Codigo esperado 200, pero se obtuvo: {status_code}"

    #Asignamos la respuesta del API en formato JSON a la
    #variable companies
    companies = response.json()

    #Validamos que la información sea una lista de objectos
    assert isinstance(companies, list), 'La respuesta no es una lista'

    #Validamos que la lista contenga elemetos
    assert len(companies) > 0, 'La lista esta vacia'

    #Recorremos los elementos y se compara que la  estructura retornada
    #por el API se igual a la estructura esperada, definida en la variable
    #expected_schema
    for company in companies:
         validate(instance=company, schema=expected_schema),'La estructura no es valida'

