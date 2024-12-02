from datetime import datetime
import os
import json

file_game = "games.txt"
file_pembayaran = "pembayaran.txt"
file_struk = "receiptify.txt"

def file_exist():
    if not os.path.exists(file_game):
        with open(file_game, "w", encoding="utf-8") as file:
            file.write("ID, Game, harga, stok\n")
    if not os.path.exists(file_pembayaran):
        with open(file_pembayaran, "w", encoding="utf-8") as file:
            pass
    if not os.path.exists(file_struk):
        with open(file_struk, "w", encoding="utf-8") as file:
            print(json.dumps(x, indent=4))

def inputan_game():
    file_exist()
    game_id = int(input("Masukkan nomor game yang ingin ditambahkan: "))
    nama_game = input("Masukkan game yang ingin ditambahkan: ")
    harga = int(input("Masukkan harga: "))
    stok = int(input("Masukkan stok: "))

    updated_game = []
    transaksi = False

    with open(file_game, "r", encoding="utf-8") as file:
        games = file.readlines()

    for game in games:
        game_data = game.strip().split(",")
        if game_data[0] == game_id or game_data[1] == nama_game:
            harga, stok = game_data[2], game_data[3]
            tambahan_stok = int(input("Masukkan stok tambahan: "))
            new_stok = int(game_data[3]) + tambahan_stok
            updated_game.append(f"{game_data[0]}, {game_data[1]}, {game_data[2]}, {new_stok}")
            print(f"stok game '{nama_game}' telah ditambahkan menjadi '{new_stok}'.")
        else:
            updated_game.append(game_id, nama_game, harga, stok)
            print(f"game {nama_game} telah ditambahkan")


def cek_stok():
    file_exist()
    try:
        with open(file_game, "r", encoding="utf-8") as file:
            cek = file.readlines()
            print(cek)
    
    except Exception as e:
        print(e)


def main():
    file_exist()
    while True:
        inputan = input("Masukkan menu yang ingin dijalankan: ")
        if inputan == "1":
            inputan_game()
        elif inputan == "2":
            cek_stok()
        else:
            continue

if __name__ == "__main__":
    main()

