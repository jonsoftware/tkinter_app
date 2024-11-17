import tkinter as tk
from tkinter import ttk

def verificar_texto(event=None):
    # Obtém o texto digitado
    texto_digitado = entrada.get("1.0", tk.END).strip()
    
    # Limpa o widget de entrada para reestilizar o texto
    entrada.tag_remove("certo", "1.0", tk.END)
    entrada.tag_remove("errado", "1.0", tk.END)
    
    # Compara caractere por caractere
    for i, (char_digitado, char_correto) in enumerate(zip(texto_digitado, codigo_referencia)):
        if char_digitado == char_correto:
            entrada.tag_add("certo", f"1.{i}", f"1.{i+1}")
        else:
            entrada.tag_add("errado", f"1.{i}", f"1.{i+1}")
    
    # Configura as cores para as tags
    entrada.tag_configure("certo", foreground="green")
    entrada.tag_configure("errado", foreground="red")

# Código de exemplo para treino
codigo_referencia = """python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\activate
pip install django
django-admin startproject setup .
python manage.py startapp todos"""

# Interface gráfica
root = tk.Tk()
root.title("Treino de Digitação - Código")
root.geometry("800x600")  # Define um tamanho inicial
root.resizable(True, True)  # Permite redimensionar a janela

# Instruções
ttk.Label(root, text="Digite o código abaixo exatamente como está:").pack(anchor="w", padx=10, pady=10)

# Área de exibição do código de exemplo
codigo_label = tk.Text(root, height=5, wrap="none", bg="#f4f4f4", font=("Courier New", 14))
codigo_label.pack(fill="both", expand=True, padx=10, pady=5)
codigo_label.insert("1.0", codigo_referencia)
codigo_label.configure(state="disabled")

# Área de entrada do usuário
entrada = tk.Text(root, height=15, wrap="none", font=("Courier New", 14))
entrada.pack(fill="both", expand=True, padx=10, pady=5)
entrada.bind("<KeyRelease>", verificar_texto)

root.mainloop()
