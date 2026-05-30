
import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        peso = float(entry_peso.get().replace(",", "."))
        altura = float(entry_altura.get().replace(",", "."))
        if altura <= 0 or peso <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "Informe peso e altura válidos.")
        return

    imc = peso / (altura ** 2)
    label_resultado["text"] = f"IMC: {imc:.2f}"

janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("300x180")
janela.resizable(False, False)

frame = tk.Frame(janela, padx=10, pady=10)
frame.pack(expand=True, fill="both")

tk.Label(frame, text="Peso (kg):").grid(row=0, column=0, sticky="w", pady=5)
entry_peso = tk.Entry(frame)
entry_peso.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Altura (m):").grid(row=1, column=0, sticky="w", pady=5)
entry_altura = tk.Entry(frame)
entry_altura.grid(row=1, column=1, pady=5)

botao_calcular = tk.Button(frame, text="Calcular IMC", command=calcular_imc)
botao_calcular.grid(row=2, column=0, columnspan=2, pady=10)

label_resultado = tk.Label(frame, text="IMC: ", font=("Arial", 12, "bold"))
label_resultado.grid(row=3, column=0, columnspan=2, pady=5)

janela.mainloop()
