from inspect import Parameter
from wsgiref import headers
from bs4 import BeautifulSoup
import requests

header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0'}

def bitcoin():
    header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0'}
    link = requests.get('https://www.google.com/search?channel=fs&client=ubuntu&q=bitcoin', headers=header)
    soup = BeautifulSoup(link.content, 'html.parser')
    btc = soup.find_all('span', attrs={'class':'pclqee'})[0]
    variacao_btc = soup.find_all('span', attrs={'jsname':'SwWl3d'})[0]
    linkn = requests.get("https://news.google.com/search?q=bitcoin%20when%3A1h&hl=pt-BR&gl=BR&ceid=BR%3Apt-419", headers=header)
    soupn = BeautifulSoup(linkn.content, 'html.parser')
    noticias = soupn.find_all("h3", attrs={"class":"ipQwMb ekueJc RD0gLb"})
    print('\n'*100)
    print('------------------------------------------')
    print(f"1 ETC ESTA VALENDO {btc.text} REAIS... \n VARIAÇÃO {variacao_btc.text} \n")
    print(f"----Principais noticícias sobre o bitcoin----\n")
    for noticia in noticias:
        print(noticia.text, "\n")
    if (noticias == []):
        print('Nenhuma notícia encontrada...\n')
    print('--------------------------------------------------\n')

def ethereum():
    link = requests.get("https://www.google.com/search?q=ethereum+valor&client=ubuntu&hs=ikC&channel=fs&sxsrf=APq-WBvTiX7M382TO-KDPpQ9yBIWRnW-Qw%3A1647833873945&ei=EfM3Yq-VOd-r1sQPyreDoAY&ved=0ahUKEwjv4dHFo9b2AhXflZUCHcrbAGQQ4dUDCA0&uact=5&oq=ethereum+valor&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAEIAEELEDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgQIABBHOgsIABCABBCxAxCDAToHCAAQsQMQQzoKCAAQsQMQgwEQQzoECAAQQ0oECEEYAEoECEYYAFDiBFiYCmCdC2gAcAJ4AIABswKIAfMDkgEHMC4xLjAuMZgBAKABAcgBCMABAQ&sclient=gws-wiz", headers=header)
    soup = BeautifulSoup(link.content, 'html.parser')
    etc = soup.find_all('span', attrs={'class':'pclqee'})[0]
    variacao_etc = soup.find_all('span', attrs={'jsname':'SwWl3d'})[0]
    linkn = requests.get("https://news.google.com/search?q=ethereum%20when%3A1h&hl=pt-BR&gl=BR&ceid=BR%3Apt-419", headers=header)
    soupn = BeautifulSoup(linkn.content, 'html.parser')
    noticias = soupn.find_all("h3", attrs={"class":"ipQwMb ekueJc RD0gLb"})
    print('\n'*100)
    print('------------------------------------------')
    print(f"1 ETC ESTA VALENDO {etc.text} REAIS... \n VARIAÇÃO {variacao_etc.text} \n")
    print(f"----Principais noticícias sobre o ethereum----\n")
    for noticia in noticias:
        print(noticia.text, "\n")
    if (noticias == []):
        print('Nenhuma notícia encontrada...\n')
    print('--------------------------------------------------\n')

def dolar():
    link = requests.get("https://www.google.com/search?channel=fs&client=ubuntu&q=dolar", headers=header)
    soup = BeautifulSoup(link.content, 'html.parser')
    dolar = soup.find_all('span', attrs={'class':'DFlfde SwHCTb'})[0]
    linkn = requests.get("https://news.google.com/search?q=dolar%20when%3A1h&hl=pt-BR&gl=BR&ceid=BR%3Apt-419", headers=header)
    soupn = BeautifulSoup(linkn.content, 'html.parser')
    noticias = soupn.find_all("h3", attrs={"class":"ipQwMb ekueJc RD0gLb"})
    print('\n'*100)
    print('------------------------------------------')
    print(f"O Dolar está valendo {dolar.text} Reais\n   ")
    print(f"----Principais noticícias sobre o dolar----\n")
    for noticia in noticias:
        print(noticia.text, "\n")
    if (noticias == []):
        print('Nenhuma notícia encontrada...\n')
    print('--------------------------------------------------\n')

def pesquisa():
    print('\n'*100)
    print('--------------------------------')
    pesq = str(input("Dígite sua pesquisa:"))
    print('--------------------------------')
    link = requests.get('https://news.google.com/search?q='+pesq+'%20when%3A1h&hl=pt-BR&gl=BR&ceid=BR%3Apt-419',headers=header)
    soup = BeautifulSoup(link.content, 'html.parser')
    noticias = soup.find_all("h3", attrs={"class":"ipQwMb ekueJc RD0gLb"})
    print(f"----Principais noticícias sobre sua pesquisa----\n")
    for noticia in noticias:
        print(noticia.text, "\n")
    if (noticias == []):
        print('Nenhuma notícia encontrada...\n')
    print('--------------------------------------------------\n')        

def horario():
    link = requests.get("https://www.google.com/search?channel=fs&client=ubuntu&q=dia+atual", headers=header)
    soup = BeautifulSoup(link.content, 'html.parser')
    data = soup.find_all("div", attrs={'class':'vk_gy vk_sh'})[0]
    link1 = requests.get("https://www.google.com/search?channel=fs&client=ubuntu&q=horario+atual", headers=header)
    soup1 = BeautifulSoup(link1.content, 'html.parser')
    hora = soup1.find_all("div", attrs={'class':'gsrt vk_bk FzvWSb YwPhnf'})[0]
    print(f"Cotação e noticías do dia {data.text} as {hora.text}")

def op(op):
    on = True
    while (on == True):
        if (op == 1):
            bitcoin()
            on = False
        if (op == 2):
            ethereum()
            on = False
        if (op == 3):
            dolar()
            on = False
        if (op == 4):
            pesquisa()
            on = False
        if(on == True):
            print("ERRO, Dígite uma opção valida:")
            print("-------------------------------")
            menu()
            op = int(input())

def sair(s):
    t = True
    while (t == True):
        if(s != 's'):
            print("Obrigado por usar volte sempre.")
            exit()
        if (s == 's'):
            print("\n"*200)
            t = False

def menu():
    print('-'*10,"MONITORAMENTO DE MOEDAS By:@ucarlux",'-'*10)
    horario()
    print('------------------------------------------------------')
    print('ESCOLHA O QUE VOCÊ QUER FAZER:')
    print('---------------------------------------------------------')
    print('DIGITE 1 PARA VER A COTAÇÃO DO BITCOIN.')
    print('DIGITE 2 PARA VER A COTAÇÃO DO ETHEREUM.')
    print('DÍGITE 3 PARA VER A COTAÇÃO DO DOLAR.')
    print('DÌGITE 4 PARA FAZER UMA PESQUISA.')
    print('----------------------------------------------------------\n')

        


s = 's'
while (s == 's'):
    menu()
    opc = int(input())
    print('\n'*100)
    print('----------------------------------------------------------')
    print("CARREGANDO AGUARDE...")
    print('----------------------------------------------------------')
    print('\10')
    op(opc)
    opc = 0
    s = input("Dìgite s para continuar ou qualquer outra tecla para saír: ")
    sair(s)



    


