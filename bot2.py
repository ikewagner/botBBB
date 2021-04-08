import requests
from bs4 import BeautifulSoup


page = requests.get("https://tvefamosos.uol.com.br/noticias/redacao/2021/04/05/eliminado-decimo-paredao-bbb-21.htm")


soup = BeautifulSoup(page.content,'html.parser')
print("\n")
print("Bot ike informa resultado parcial BBB21 ")
print("Atualizado cada 1/hr ")
print("-----------------------------------------------------------")

nomeprimeiro = soup.find('label', attrs={'for': "radio-904803"})
print("\n")
print(nomeprimeiro.text)
primeiro = soup.find('span', attrs={'ng-bind': "percLbl904803"})
print(primeiro.text)



nomesegundo = soup.find('label', attrs={'for': "radio-904805"})
print("\n")
print(nomesegundo.text)
segundo = soup.find('span', attrs={'ng-bind': "percLbl904805"})
print(segundo.text)



nometerceiro = soup.find('label', attrs={'for': "radio-904804"})
print("\n")
print(nometerceiro.text)
terceiro = soup.find('span', attrs={'ng-bind': "percLbl904804"})
print(terceiro.text)


votos = soup.find('span', attrs={'ng-bind': "totalVotes"})
print("\nTotal de votos:",votos.text)
print("#bbb21")




