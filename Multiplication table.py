import tkinter as tk

def show_output():
    number = int(number_input.get())
    
    if number == 0:
        output_label.configure(text='ศูนย์อะไรไม่เท่าเสียศูนย์')
        return

# ไม่ใช่ break เพราะไม่ใช่ loop

    output = ''
    for i in range(1,13):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(number * i) + '\n'
    output_label.configure(text=output)

# /n คือ เว้นบรรทัด

window = tk.Tk()
window.title('Packkymugi')
window.minsize(width=400, height=400)

title_lable = tk.Label(master=window, text = 'Multiplication table')
title_lable.pack(pady=10)

number_input = tk.Entry(master=window, width = 20)
number_input.pack(pady=10)

go_button = tk.Button(
    master = window, text = 'Click!',
    command = show_output, width = 10 , height = 2
    )
go_button.pack(pady=10)

output_label = tk.Label(master=window)
output_label.pack(pady=10)

# padx / pady คือ เว้นช่องไฟตามแกน x , y ตามแต่ใจต้องการ

window.mainloop()
