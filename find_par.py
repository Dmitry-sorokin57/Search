# Собираем параметры для запроса к StaticMapsAPI:
def find_params(toponym_longitude, toponym_lattitude, delta1, delta2):
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([delta1, delta2]),
        "l": "map",
        "pt": f"{toponym_longitude},{toponym_lattitude},org"
    }
    return map_params