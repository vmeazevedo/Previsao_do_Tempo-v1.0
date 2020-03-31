## Previsão do Tempo v1.0
Aplicação de previsão do tempo utilizando as JSON Geolocation Web Service para identificar a localizar e o AccuWeather para apresentar as informações meteorológicas.

## Exemplo de funcionamento do código:
![previsão](https://user-images.githubusercontent.com/40063504/78058900-63b33e00-735f-11ea-96d8-6b7606faedf8.PNG)

## Requesitos para rodar o código:
- Python 3.8
- Instalação das bibliotecas (caso não as tenha): request + json + pprint

- Ir até o site da Geoplugin - JSON Geolocation Web Service, e pegar o endereço da requisição a qual iremos fazer:
Site: https://www.geoplugin.com/webservices/json
Endereço da requisição: http://www.geoplugin.net/json.gp

- Acessar o site da AccuWeather e se registrar:
Site: https://www.developer.accuweather.com/

- Acessar o site devidamente registrador e ir no menu "My Apps" para criarmos um novo app.
  - Add new app
  - Preencher o cadastro de informações de como o app irá funcionar.
  - Após preencher, clicar em Create App.
  - Com seu novo app criado agora você tem acesso a uma API Key que será necessário para rodarmos o código.
  
  Obs: O limited trial só permite a utilização do código 50 vezes por dia, por isso por gentileza realize o passo anterior para obter um API Key para você e com a API Key em mãos substitua a varial 'accuweatherAPIKey' no início do código com a sua API Key.

