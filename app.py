# Programa para calcular consumo mensal de energia

# Entrada de dados
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horasDia = float(input("Digite o tempo médio de uso diário em horas: "))

# Cálculo do consumo mensal em kWh
consumoMensal = (potencia * horasDia * 30) / 1000

# Cálculo do custo estimado (valor fixo de R$ 0,75 por kWh)
custoEstimado = consumoMensal * 0.75

# Saída formatada
print("\n--- Resultado ---")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumoMensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custoEstimado:.2f}/mês")
