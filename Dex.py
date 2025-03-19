from cProfile import label

from tkinter import *
from tkinter import ttk

# importando Pillow
from PIL import Image, ImageTk

from Dados import *

############## colors ##############
co0 = "#444466"  # black
co1 = "#FFFFFF"  # white
co2 = "#0000FF"  # blue
co3 = "#38576B"  # valor
co4 = "#403d3d"  # leters
co5 = "#af5350"  # red

# criando janela
janela = Tk()
janela.title('')
janela.geometry('960x720')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

# criando frame
frame_pokemon = Frame(janela,width=960, height=400, relief='flat')
frame_pokemon.grid(row=1, column=0)


def trocar_sprite(i):
    global imagem_Sprite, sprite_imagem

    #switch background
    frame_pokemon['bg'] = pokemon[i]['Group'][3]

    # sprite switch
    name_sprite['text'] = i
    name_sprite['bg'] = pokemon[i]['Group'][3]
    name_group['text'] = pokemon[i]['Group'][1]
    name_group['bg'] = pokemon[i]['Group'][3]
    id_number['text'] = pokemon[i]['Group'][0]
    id_number['bg'] = pokemon[i]['Group'][3]

    imagem_Sprite = pokemon[i]['Group'][2]

    # imagem trainer
    imagem_Sprite = Image.open(imagem_Sprite)
    imagem_Sprite = imagem_Sprite.resize((238, 238))
    imagem_Sprite = ImageTk.PhotoImage(imagem_Sprite)

    sprite_imagem = Label(frame_pokemon, image=imagem_Sprite, relief='flat', anchor=CENTER, bg=pokemon[i]['Group'][3], fg=co1)
    sprite_imagem.place(x=100, y=90)

    # Status Sprite
    poke_hp['text'] = pokemon[i]['Status'][0]
    poke_attack['text'] = pokemon[i]['Status'][1]
    poke_defense['text'] = pokemon[i]['Status'][2]
    poke_SpAtk['text'] = pokemon[i]['Status'][3]
    poke_SpDef['text'] = pokemon[i]['Status'][4]
    poke_speed['text'] = pokemon[i]['Status'][5]
    poke_total['text'] = pokemon[i]['Status'][6]

    # Abilitys Sprite
    poke_ability1['text'] = pokemon[i]['Ability'][0]
    poke_ability2['text'] = pokemon[i]['Ability'][1]
    poke_ability3['text'] = pokemon[i]['Ability'][2]






# name trainer
name_sprite = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys 20'), fg=co1)
name_sprite.place(x=12, y=15)

# Group
name_group = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 14'), fg=co1)
name_group.place(x=12, y=60)

# id
id_number = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 13'), fg=co1)
id_number.place(x=12, y=95)



# Status
poke_status = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
poke_status.place(x=25, y=410)

# Hp
poke_hp= Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 14'), bg=co1, fg=co4)
poke_hp.place(x=25, y=460)

# Attack
poke_attack= Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 14'), bg=co1, fg=co4)
poke_attack.place(x=25, y=460)

# Defense
poke_defense= Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 14'), bg=co1, fg=co4)
poke_defense.place(x=25, y=490)

# SpAtk
poke_SpAtk= Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 14'), bg=co1, fg=co4)
poke_SpAtk.place(x=25, y=520)

# SpDef
poke_SpDef= Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 14'), bg=co1, fg=co4)
poke_SpDef.place(x=25, y=550)

# Speed
poke_speed= Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 14'), bg=co1, fg=co4)
poke_speed.place(x=25, y=580)

# Total
poke_total= Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 14'), bg=co1, fg=co4)
poke_total.place(x=25, y=630)

# Ability
poke_ability = Label(janela, text='Abilitys', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
poke_ability.place(x=260, y=410)

# Ability 1
poke_ability1= Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 14'), bg=co1, fg=co4)
poke_ability1.place(x=260, y=460)

# Ability 2
poke_ability2= Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 14'), bg=co1, fg=co4)
poke_ability2.place(x=260, y=490)

# Hidden Ability
poke_ability3= Label(janela, text='', relief='flat', anchor=CENTER, font=('Verdana 14'), bg=co1, fg=co4)
poke_ability3.place(x=260, y=520)



# create buttons

# buttom trainer
bt_figure_trainer = Image.open('Badges/AshKetchum.png')
bt_figure_trainer = bt_figure_trainer.resize((40, 40))
bt_figure_trainer = ImageTk.PhotoImage(bt_figure_trainer)

bt_figure_image = Button(janela,command=lambda:trocar_sprite("Ash Ketchum"),image=bt_figure_trainer, text="Ash Ketchum",width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 12', bg=co1, fg=co0)
bt_figure_image.place(x=790, y=10)

# buttom pokemon
bt_figure_pokemon1 = Image.open('Project/PikachuS.webp')
bt_figure_pokemon1 = bt_figure_pokemon1.resize((40, 40))
bt_figure_pokemon1 = ImageTk.PhotoImage(bt_figure_pokemon1)

bt_figure_image = Button(janela,command=lambda:trocar_sprite("Pikachu"),image=bt_figure_pokemon1, text="Pikachu",width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 12', bg=co1, fg=co0)
bt_figure_image.place(x=790, y=65)

# buttom pokemon 2
bt_figure_pokemon2 = Image.open('Project/GreninjaS.webp')
bt_figure_pokemon2 = bt_figure_pokemon2.resize((40, 40))
bt_figure_pokemon2 = ImageTk.PhotoImage(bt_figure_pokemon2)

bt_figure_image = Button(janela,command=lambda:trocar_sprite("Greninja"),image=bt_figure_pokemon2, text="Greninja",width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 12', bg=co1, fg=co0)
bt_figure_image.place(x=790, y=120)

# buttom pokemon 3
bt_figure_pokemon3 = Image.open('Project/TalonflameS.webp')
bt_figure_pokemon3 = bt_figure_pokemon3.resize((40, 40))
bt_figure_pokemon3 = ImageTk.PhotoImage(bt_figure_pokemon3)

bt_figure_image = Button(janela,command=lambda:trocar_sprite("Talonflame"),image=bt_figure_pokemon3, text="Talonflame",width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 12', bg=co1, fg=co0)
bt_figure_image.place(x=790, y=175)

# buttom pokemon 4
bt_figure_pokemon4 = Image.open('Project/HawluchaS.webp')
bt_figure_pokemon4 = bt_figure_pokemon4.resize((40, 40))
bt_figure_pokemon4 = ImageTk.PhotoImage(bt_figure_pokemon4)

bt_figure_image = Button(janela,command=lambda:trocar_sprite("Hawlucha"),image=bt_figure_pokemon4, text="Hawlucha",width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 12', bg=co1, fg=co0)
bt_figure_image.place(x=790, y=230)

# buttom pokemon 5
bt_figure_pokemon5 = Image.open('Project/NoivernS.webp')
bt_figure_pokemon5 = bt_figure_pokemon5.resize((40, 40))
bt_figure_pokemon5 = ImageTk.PhotoImage(bt_figure_pokemon5)

bt_figure_image = Button(janela,command=lambda:trocar_sprite("Noivern"),image=bt_figure_pokemon5, text="Noivern",width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 12', bg=co1, fg=co0)
bt_figure_image.place(x=790, y=285)

# buttom pokemon 6
bt_figure_pokemon6 = Image.open('Project/GoodraS.webp')
bt_figure_pokemon6 = bt_figure_pokemon6.resize((40, 40))
bt_figure_pokemon6 = ImageTk.PhotoImage(bt_figure_pokemon6)

bt_figure_image = Button(janela,command=lambda:trocar_sprite("Goodra"),image=bt_figure_pokemon6, text="Goodra",width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 12', bg=co1, fg=co0)
bt_figure_image.place(x=790, y=340)




######### INSÍGNIAS ########

# Insígnia Topic
poke_bagdes = Label(janela, text='Badges', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
poke_bagdes.place(x=525, y=410)

# buttom badge 1
bt_figure_badge = Image.open('Badges/First.png')
bt_figure_badge = bt_figure_badge.resize((45, 45))
bt_figure_badge = ImageTk.PhotoImage(bt_figure_badge)

bt_figure_image = Button(janela, image=bt_figure_badge, text="Bug Badge",width=140, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 10', bg=co1, fg=co0)
bt_figure_image.place(x=415, y=450)

# buttom badge 2
bt_figure_badge2 = Image.open('Badges/Second.png')
bt_figure_badge2 = bt_figure_badge2.resize((45, 45))
bt_figure_badge2 = ImageTk.PhotoImage(bt_figure_badge2)

bt_figure_image = Button(janela, image=bt_figure_badge2, text="Cliff Badge",width=140, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 10', bg=co1, fg=co0)
bt_figure_image.place(x=415, y=510)

# buttom badge 3
bt_figure_badge3 = Image.open('Badges/Third.png')
bt_figure_badge3 = bt_figure_badge3.resize((45, 45))
bt_figure_badge3 = ImageTk.PhotoImage(bt_figure_badge3)

bt_figure_image = Button(janela, image=bt_figure_badge3, text="Rumble Badge",width=140, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 10', bg=co1, fg=co0)
bt_figure_image.place(x=415, y=570)

# buttom badge 4
bt_figure_badge4 = Image.open('Badges/Fourth.png')
bt_figure_badge4 = bt_figure_badge4.resize((45, 45))
bt_figure_badge4 = ImageTk.PhotoImage(bt_figure_badge4)

bt_figure_image = Button(janela, image=bt_figure_badge4, text="Plant Badge",width=140, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 10', bg=co1, fg=co0)
bt_figure_image.place(x=415, y=630)

# buttom badge 5
bt_figure_badge5 = Image.open('Badges/Fiveth.png')
bt_figure_badge5 = bt_figure_badge5.resize((45, 45))
bt_figure_badge5 = ImageTk.PhotoImage(bt_figure_badge5)

bt_figure_image = Button(janela, image=bt_figure_badge5, text="Voltage Badge",width=140, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 10', bg=co1, fg=co0)
bt_figure_image.place(x=590, y=450)

# buttom badge 6
bt_figure_badge6 = Image.open('Badges/Sixth.png')
bt_figure_badge6 = bt_figure_badge6.resize((45, 45))
bt_figure_badge6 = ImageTk.PhotoImage(bt_figure_badge6)

bt_figure_image = Button(janela, image=bt_figure_badge6, text="Fairy Badge",width=140, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 10', bg=co1, fg=co0)
bt_figure_image.place(x=590, y=510)

# buttom badge 7
bt_figure_badge7 = Image.open('Badges/Seventh.png')
bt_figure_badge7 = bt_figure_badge7.resize((45, 45))
bt_figure_badge7 = ImageTk.PhotoImage(bt_figure_badge7)

bt_figure_image = Button(janela, image=bt_figure_badge7, text="Psychic Badge",width=140, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 10', bg=co1, fg=co0)
bt_figure_image.place(x=590, y=570)

# buttom badge 8
bt_figure_badge8 = Image.open('Badges/Eighth.png')
bt_figure_badge8 = bt_figure_badge8.resize((45, 45))
bt_figure_badge8 = ImageTk.PhotoImage(bt_figure_badge8)

bt_figure_image = Button(janela, image=bt_figure_badge8, text="Iceberg Badge",width=140, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font='Verdana 10', bg=co1, fg=co0)
bt_figure_image.place(x=590, y=630)


trocar_sprite('Ash Ketchum')
















































janela.mainloop()