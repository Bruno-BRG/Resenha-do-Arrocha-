class Tigrinho:
    def __init__(self):
        self.filho_da_puta = False

    def solta_a_carta(self):
        return True

class EU:
    def __init__(self):
        self.opening = "Solta a carta caralho, tigrinho filha da puta"

    def pegar_meudinheiro(self):
        print("Pra eu pegar o meu dinheiro")

    def comer(self, putas):
        print(f"e comer umas {putas}")

tigrinho = Tigrinho()
eu = EU()

def vuk_vuk(quantidade):
    print("é")
    for _ in range(quantidade):
        print("vuk vuk")

def na_onda_maluka(quantidade):
    vuk_vuk(quantidade)     
    print("Na onda maluka")

def yeah(quantidade):
    vuk_vuk(quantidade)
    print("yeah")

def solta_a_carta():
    if not tigrinho.solta_a_carta():
        tigrinho.filho_da_puta = True
    else:
        eu.pegar_meudinheiro()

def resto():
    for _ in range(2):
        print(eu.opening)
        solta_a_carta() 
    eu.comer("4 puta") 
    na_onda_maluka(2)  
    yeah(2)
    na_onda_maluka(2)
    vuk_vuk(1) 

def tigrinho_filho_da_puta():
    value = input("Digite 1 se o tigrinho nao é filho da puta ou 2 para caso ele seja filha da puta: ")
    if value == "1":
        tigrinho.filho_da_puta = True
    else:
        tigrinho.filho_da_puta = False

def main():
    tigrinho_filho_da_puta()
    if tigrinho.filho_da_puta:
        resto() 
    else:
        print("O Tigrinho e filho da puta e nao vai te dar o seu dinheiro")

if __name__ == "__main__":
    main()
