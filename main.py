import datetime
import pandas as pd
import requests as req
import time

# expires in one hour
TOKEN = "eyJ4NXQiOiJNalJqWkRRMU1EQmtPR1JqWW1Jek9EVmxaRFEzWkdFeU1EVTVabU5rWldVeU9XUmhPRFZpTnciLCJraWQiOiJNRGN5WVdFNU16ZzVaVFJrT1dVME1XWTBNVE0xTkdJMllqbG1OVFZrT0dJd01UVmlORGRpWldJM1pEUmpZVEpsTTJaa05Ua3dNR1F3TWpZeVlXTmxNQV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJhdXRlbnRpa3VzIiwiYXV0IjoiQVBQTElDQVRJT04iLCJhdWQiOiJYUmNnZXZSdVEwN1dLRkpRbnk3Rk5MUkdhZjBhIiwibmJmIjoxNzM2NzkxNDE1LCJhenAiOiJYUmNnZXZSdVEwN1dLRkpRbnk3Rk5MUkdhZjBhIiwic2NvcGUiOiJkZWZhdWx0IiwiaXNzIjoiaHR0cHM6XC9cL3B1Ymxpc2hlci5hcGlzZXJwcm8uc2VycHJvLmdvdi5icjo0NDNcL29hdXRoMlwvdG9rZW4iLCJyZWFsbSI6eyJzaWduaW5nX3RlbmFudCI6ImNhcmJvbi5zdXBlciJ9LCJleHAiOjE3MzY3OTUwMTUsImlhdCI6MTczNjc5MTQxNSwianRpIjoiZTVmZjhjZjItNzRhZC00ODE0LWJmNTQtZTgxZmEyNjUzY2E5In0.iHxUQ4iyujwfKBCOlmewGFRS6sgtOBMz3ykNUPLd1ts2RCC9oCZ9HIqHFGzP0sMKUxy_vrF26gQWzMCrGvoLmzp8LkNnrmRgbhAAvu5AFBHXtvfIENzrrKlS16xS4NEau-QO2u7w_zJuL8YfbF0bZp8g4InPORGQp9qrCFaHLQ6wdbA-eA0VVGpfmr62hGJXiVa7QS96eNCQTanL9fLgIdblVAGzKi8kbjX5ZZuPpmuY3UZ8KMZWXjTPcoIINeFKjvWBnzyBWrNkLgZfGqkaqlkUN_wL-3ngEusZuIr5F0kHr8SaE-7D50C1vj0dj9EkyFgQaEn4baGcj80blKBbnQ"


MOCK = {
    "40442820135": {
        "ni": "40442820135",
        "nome": "Nome do CPF 404.428.201-35",
        "situacao": {"codigo": "0", "descricao": "Regular"},
        "nascimento": "14111970",
    },
    "63017285995": {
        "ni": "63017285995",
        "nome": "Nome do CPF 630.172.859-95",
        "situacao": {"codigo": "0", "descricao": "Regular"},
        "nascimento": "26121964",
    },
    "91708635203": {
        "ni": "91708635203",
        "nome": "Nome do CPF 917.086.352-03",
        "situacao": {"codigo": "0", "descricao": "Regular"},
        "nascimento": "03011943",
    },
    "58136053391": {
        "ni": "58136053391",
        "nome": "Nome do CPF 581.360.533-91",
        "situacao": {"codigo": "0", "descricao": "REGULAR"},
        "nascimento": "20111972",
    },
    "40532176871": {
        "ni": "40532176871",
        "nome": "Nome do CPF 405.321.768-71",
        "situacao": {"codigo": "2", "descricao": "Suspensa"},
        "nascimento": "22031982",
    },
    "47123586964": {
        "ni": "47123586964",
        "nome": "Nome do CPF 471.235.869-64",
        "situacao": {"codigo": "2", "descricao": "Suspensa"},
        "nascimento": "29051940",
    },
    "07691852312": {
        "ni": "07691852312",
        "nome": "Nome do CPF 076.918.523-12",
        "situacao": {"codigo": "4", "descricao": "Pendente de Regularização"},
        "nascimento": "13082000",
    },
    "10975384600": {
        "ni": "10975384600",
        "nome": "Nome do CPF 109.753.846-00",
        "situacao": {"codigo": "4", "descricao": "Pendente de Regularização"},
        "nascimento": "01091975",
    },
    "01648527949": {
        "ni": "01648527949",
        "nome": "Nome do CPF 016.485.279-49",
        "situacao": {"codigo": "5", "descricao": "Cancelada por Multiplicidade"},
        "nascimento": "18021996",
    },
    "47893062592": {
        "ni": "47893062592",
        "nome": "Nome do CPF 478.930.625-92",
        "situacao": {"codigo": "5", "descricao": "Cancelada por Multiplicidade"},
        "nascimento": "21031986",
    },
    "98302514705": {
        "ni": "98302514705",
        "nome": "Nome do CPF 983.025.147-05",
        "situacao": {"codigo": "8", "descricao": "Nula"},
        "nascimento": "05101999",
    },
    "18025346790": {
        "ni": "18025346790",
        "nome": "Nome do CPF 180.253.467-90",
        "situacao": {"codigo": "8", "descricao": "Nula"},
        "nascimento": "140712001",
    },
    "64913872591": {
        "ni": "64913872591",
        "nome": "Nome do CPF 649.138.725-91",
        "situacao": {"codigo": "9", "descricao": "Cancelada de Oficio"},
        "nascimento": "22041956",
    },
    "52389071686": {
        "ni": "52389071686",
        "nome": "Nome do CPF 523.890.716-86",
        "situacao": {"codigo": "9", "descricao": "Cancelada de Oficio"},
        "nascimento": "27051942",
    },
    "05137518743": {
        "ni": "05137518743",
        "nome": "Nome do CPF 051.375.187-43",
        "situacao": {"codigo": "3", "descricao": "TITULAR FALECIDO"},
        "nascimento": "05071965",
        "obito": "2019",
    },
    "08849979878": {
        "ni": "08849979878",
        "nome": "Nome do CPF 088.499.798-78",
        "situacao": {"codigo": "3", "descricao": "TITULAR FALECIDO"},
        "nascimento": "23031980",
        "obito": "2020",
    },
}


def main() -> None:
    now = datetime.datetime.now()
    timestamp = f"{now.date()}T{now.timestamp()}"
    input_df = pd.read_csv("excluidos-202412.csv", dtype=str)

    # info_by_cpf = MOCK
    info_by_cpf = {}
    for i, cpf in enumerate(input_df["CPF"][10:]):
        try:
            queried = query_serpro(cpf)

            info_by_cpf[cpf] = {
                **queried,
                **queried["situacao"],
            }
            print(f"{i} {queried}")
            time.sleep(0.6)
        except Exception:
            info_df = pd.DataFrame.from_dict(info_by_cpf, orient="index")
            info_df.to_csv(f"{timestamp}-cpfs.csv")
    else:
        info_df = pd.DataFrame.from_dict(info_by_cpf, orient="index")
        info_df.to_csv(f"{timestamp}-cpfs.csv")

    return


def query_serpro(cpf: str):
    base_url = "https://gateway.apiserpro.serpro.gov.br/consulta-cpf-df/v1/cpf"
    res = req.get(
        f"{base_url}/{cpf}",
        headers={"accept": "application/json", "Authorization": f"Bearer {TOKEN}"},
    )

    return res.json()


if __name__ == "__main__":
    main()
