import tkinter as tk

root = tk.Tk()
root.title("Mad GunZ Players")

canvas = tk.Canvas(root, width=1200, height=800, bg="#111111")
canvas.pack()

canvas.create_text(600, 50, text="MAD GUNZ PLAYERS (WORLDWIDE)", fill="#FFFFFF", font=("Impact", 45))
tos_text = """
1. Voidwalker
2. Cropsecrack
3. Michi
4. Muki God of War
5. Javad God of War
6. Frost
7. Entitinull303
8. Snaip
9. Darkness
10. Tech the warrior """

canvas.create_text(100, 200, text=tos_text, fill="#FFFFFF", font=("Fraktur", 10, "bold"))
canvas.create_text(600, 650, text="CONTACT US TO GET YOUR USERNAME ADDED TOO: demon.cropsecrack.god.of.war.mg@gmail.com (or) cropsecrack@Gmail.com", fill="#FFFFFF", font=("Impact", 14))
root.mainloop()
