# Задача

smart_watch = 600
phone = 1000
playstation = 450
laptop = 1550
music_player = 400
tablet = 400
money = 1300
# Хочет купить music_player = 400 smart_watch = 600 playstation = 450. Есть 1300, третий товар со скидкой 30%,
# если купить на 1000

if smart_watch + music_player >= 1000:
    playstation_sale = playstation / 3 * 2
    if smart_watch + music_player + playstation_sale == money:
        print("Yes")
    else:
        print("No")

elif smart_watch + music_player < 1000:
    playstation_sale = playstation
    if smart_watch + music_player + playstation_sale == money:
        print("Yes")
    else:
        print("No")
