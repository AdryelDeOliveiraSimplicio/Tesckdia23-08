cargos = ["gerente", "analista", "estagiario"]

cargo_funcionario = input("Qual é o seu cargo? ")
dia_semana = input("Qual é o dia da semana? ")

if cargo_funcionario.lower() == "gerente":
    print("Acesso irrestrito você pode entrar!")
elif cargo_funcionario.lower() == "estagiario":
    if dia_semana.lower() not in ["sábado", "domingo"]:
        print("Pode entrar!")
    else:
        print("Acesso negado!")
else:
    print("Cargo não reconhecido.")