
#kata sambutan...
def space():
    space = "\n" *50
    print(space)

def kataSambutan():
    print("""
    ******************************
    * P A K O N G >> O N L I N E *
    ******************************
      copy right raja serah 2018

        >> by raja serah <<

    Keuntungan ditangan anda..
    kami berikan Free Rp.100.000

    Yang menang untung...
    Yang kalah untung...

    But Carabut Cabuuuuuttttt...
    """)

def menu():
    print("""
    --------------------------
      masukan pilihan anda
    --------------------------
    1 >> Main Pakong Online
    2 >> Tentang Pakong Online
    3 >> Cek saldo Anda
    4 >> Buat akun baru
    5 >> Keluar

    """)

    while True:
        x = input("masukan pilihan anda: ")

        if x == "1":
            login()
        elif x == "2":
            tentangPakong()
        elif x == "3":
            login()
        elif x == "4":
            register()
        elif x == "5":
            exit()
        elif x == '':
            menu()


def login():

    while True:
        username = input("masukan username anda: ")
        password = input("masukan password anda: ")

        with open("username.txt", "r") as usr:
            validUsr = usr.read().splitlines()

        with open("password.txt", "r") as pas:
            validPas = pas.read().splitlines()


        if username in validUsr and password in validPas:
            mainPakong()
        else:
            space()
            print("username atau password salah..!!")
            menu()
