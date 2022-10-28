from rich import print
import os

VOTOS_BOLSONARO = 0
VOTOS_LULA = 0
VOTOS_NULO = 0

while True:
    print('*' * 20)
    print(f"ELEIÇÕES 2022")
    print(f"""[on green]TOTAL BOLSONARO:[/]{VOTOS_BOLSONARO}{os.linesep}[on red]TOTAL LULA:[/]{VOTOS_LULA}{os.linesep}[on white]TOTAL VOTOS NULOS:[/]{VOTOS_NULO}""")
    print('*' * 20)
    
    voto = int(input(f"""Para quem gostaria de votar ?{os.linesep}22 - Bolsonaro{os.linesep}13 - Lula {os.linesep}00 - Votar nulo {os.linesep}Seu voto: """   
        ))
    
    if voto == 22:
        VOTOS_BOLSONARO += 1
    elif voto == 13:
        VOTOS_LULA += 1
    elif voto == 00:
         VOTOS_NULO += 1
    else:
        os.system("cls")
        input("Opcao inválida, pressione qualquer tecla para continuar... ")
    os.system("cls")