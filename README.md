Use a biblioteca tkinter para melhor usabilidade da janela
IDE > from tkinter import *
IDE > from tkinter import ttk


Use a biblioteca Pillow para importar imagens
Terminal > pip install Pillow
IDE > from PIL import Image, ImageTk

Use o cProfile para uma craição de perfil mais fluída
IDE > from cProfile import label

Bom... basicamente essa é a explicação basica por trás do projeto, logo abaixo estará escrita a parte mais importante do código, mas no repositório irá ter completo, inclusive com os dados e as imagens anexadas


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
