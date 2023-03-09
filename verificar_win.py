import tkinter as tk
from tkinter import font
import platform
import psutil
import os

def check_system():
    os_type = "64X" if "64" in platform.architecture()[0] else "32X"
    os_version = "OK" if int(platform.release()) > 7 else "FAIL"
    ram = "OK" if psutil.virtual_memory().total >= 4 * 1024 * 1024 * 1024 else "FAIL"
    disk = "OK" if psutil.disk_usage('/').total >= 60 * 1024 * 1024 * 1024 else "FAIL"
    result_label.config(text=f"Sistema Operacional: {os_type}\nVersão do Sistema: {os_version}\nRAM: {psutil.virtual_memory().total / (1024 * 1024 * 1024):.2f} GB\nDisco: {disk}")
    if ram == "OK" and disk == "OK" and os_version == "OK":
        result_label.config(fg="green", font=bold_font)
    else:
        result_label.config(fg="red", font=bold_font)

def optimize_mysql():
    total_ram = psutil.virtual_memory().total
    ram_in_mb = total_ram / (1024 * 1024)
    ram_otm = int(ram_in_mb * 0.375)
    innodb_buffer_pool_size = f"{ram_otm:.0f}M"
    with open(r"c:\mysql\my.ini", "r+") as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in lines:
            if line.startswith("max_connections"):
                if "server-id = 1" in line:
                    f.write("max_connections=1200\n")
                else:
                    f.write("max_connections=900\n")
            elif line.startswith("innodb_buffer_pool_size"):
                f.write(f"innodb_buffer_pool_size={innodb_buffer_pool_size}\n")
            else:
                f.write(line)
    result_label.config(text="my.ini otimizado com sucesso!\n Não foi feito o IBDATA", fg="green")



root = tk.Tk()
root.geometry("400x250")
root.title("Checar sistema")

bold_font = font.Font(family="Helvetica", size=12, weight="bold")

check_button = tk.Button(root, text="VALIDAR", font=bold_font, command=check_system)
check_button.pack(pady=10)

optimize_button = tk.Button(root, text="OTIMIZAR my.ini", font=bold_font, command=optimize_mysql)
optimize_button.pack(pady=10)

result_label = tk.Label(root, text="", font=bold_font)
result_label.pack()

root.mainloop()
