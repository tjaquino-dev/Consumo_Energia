# ⚡ Calculadora de Consumo de Energia

## 🎯 Objetivo
Este sistema tem como finalidade calcular o consumo mensal de energia elétrica de um aparelho doméstico, com base em sua potência (W) e tempo médio de uso diário (h). Além disso, estima o custo mensal considerando uma tarifa fixa de energia.

## 🖥️ Linguagem Utilizada
- **Python** 🐍

## 📐 Fórmula Utilizada
O cálculo do consumo mensal em kWh é feito pela fórmula:



\[
\text{consumoMensal} = \frac{\text{potência (W)} \cdot \text{horasDia} \cdot 30}{1000}
\]



Em seguida, o custo estimado é calculado como:



\[
\text{custoEstimado} = \text{consumoMensal} \cdot 0.75
\]



## 🚀 Instruções de Execução
1. Certifique-se de ter o **Python 3** instalado em sua máquina.  
2. Salve o código em um arquivo chamado `consumo.py`.  
3. No terminal, execute:
   ```bash
   python consumo.py
