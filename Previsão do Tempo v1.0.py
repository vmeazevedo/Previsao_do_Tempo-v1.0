import requests
import json
import pprint

accuweatherAPIKey = 'ZJYXMjCTnyAApLhwdP7Kdt2EaEw9tEnP'

r = requests.get('http://www.geoplugin.net/json.gp')

print('Bem vindo ao app de previsão do tempo v.10.')
print('Estamos obtendo as informações sobre o tempo em sua localização, por favor, aguarde um momento.\n')

if (r.status_code != 200):
    print('Não foi possível obter a localização.')
else:
    localizacao = json.loads(r.text)
    lat = localizacao['geoplugin_latitude']
    long = localizacao['geoplugin_longitude']

    LocationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/" \
                     + "search?apikey=" + accuweatherAPIKey \
                     + "&q=" + lat + "%2C"+ long +"&language=pt-br"

    r2 = requests.get(LocationAPIUrl)
    if (r.status_code != 200):
        print('Não foi possível obter a código do local.')
    else:
        locationResponse = json.loads(r2.text)
        nomeLocal = locationResponse['LocalizedName'] + ', ' \
                    + locationResponse['AdministrativeArea']['LocalizedName'] + '. ' \
                    + locationResponse['Country']['LocalizedName']
        codigoLocal = locationResponse['Key']
        print('Sua localização é: ', nomeLocal)
        
    CurrentConditionsAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/" \
                              + codigoLocal + "?apikey=" + accuweatherAPIKey \
                              + "&language=pt-br"
    r3 = requests.get(CurrentConditionsAPIUrl)
    if (r3.status_code != 200):
        print('Não foi possível obter a código do local.')
    else:
        CurrentConditionsResponse = json.loads(r3.text)
        textoClima = CurrentConditionsResponse[0]['WeatherText']
        temperatura = CurrentConditionsResponse[0]['Temperature']['Metric']['Value']
        print('Clima no momento: '+ textoClima)
        print('Temperatura: '+ str(temperatura) + " Cº")

input('\nPressione qualquer tecla para sair')
