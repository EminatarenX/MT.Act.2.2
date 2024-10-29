import tkinter as tk
from tkinter import ttk

transitions = {
    ("q0", "1"): ("q0", "1", "R"),
    ("q0", "0"): ("q1", "0", "R"),
    ("q1", "+"): ("q2", "+", "R"),
    ("q2", "0"): ("q2", "0", "R"),
    ("q2", "1"): ("q2", "1", "R"),
    ("q2", " "): ("q3", " ", "L"),  
    ("q3", "+"): ("q4", "+", "R"), 
}

def turing_machine(tape, state):
    head_position = 0 
    buffer = []  

    while state != "qf":
        symbol = tape[head_position] if head_position < len(tape) else " " 
        if (state, symbol) not in transitions:
            break  
        new_state, new_symbol, direction = transitions[(state, symbol)]
        
        if head_position < len(tape):
            tape[head_position] = new_symbol
        else:
            tape.append(new_symbol)
        
        if state == "q2" and symbol in ["0", "1"]:
            buffer.append(symbol)
        
        state = new_state
        head_position += 1 if direction == "R" else -1
        
        if head_position < 0:
            tape.insert(0, " ")
            head_position = 0
    

    number = int("".join(buffer), 2)
    result = bin(2 + number)[2:]  
    
    return result

def run_turing_machine():
    binary_input = input_field.get()
    
    # Validación del formato "10+[binary_number]"
    if not binary_input.startswith("10+"):
        result_label.config(text="Error: Formato inválido. Use '10+[binary_number]'.")
        return
    
    # Convertir la entrada en una lista de caracteres para la cinta
    tape = list(binary_input + " ")  # Añadimos un espacio en blanco al final
    
    # Ejecuta la máquina de Turing
    result = turing_machine(tape, "q0")
    
    # Agrega el input y el resultado a la tabla
    results_table.insert("", "end", values=(binary_input, result))
    result_label.config(text="")

# Crear la interfaz de Tkinter
root = tk.Tk()
root.title("Máquina de Turing - Suma de números")

# Crear los widgets de entrada y botón
input_label = tk.Label(root, text="Ingresa la suma en formato '10+[binary_number]':")
input_label.pack()

input_field = tk.Entry(root)
input_field.pack()

run_button = tk.Button(root, text="Calcular", command=run_turing_machine)
run_button.pack()

# Crear la tabla de resultados
results_table = ttk.Treeview(root, columns=("Input", "Resultado"), show="headings")
results_table.heading("Input", text="Input")
results_table.heading("Resultado", text="Resultado")
results_table.pack()

# Etiqueta para mostrar errores
result_label = tk.Label(root, text="", fg="red")
result_label.pack()

root.mainloop()
