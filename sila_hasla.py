import re

#hasło musi mieć conajmniej 8 znaków, dopuszczalne litery duże, małe, musi być liczba, musi być znak specjalny jeden z '!#$%&*'
def walidacja_pass():
    while True:
        haslo = input('Wpisz hasło: ')
        if len(haslo) < 8:
            print('Hasło musi mieć conajmniej 8 znaków.')
        elif re.search('[a-zA-Z]', haslo) is None:
            print("Hasło musi zawierać litery.")
        elif re.search('[0-9]', haslo) is None:
            print('Hasło musi mieć conajmniej 1 liczbą.')
        elif re.search('[!#$%&*]', haslo) is None:
            print('Hasło musi zawierać conajmniej 1 znak specjalny z listy: !#$%&*')
        else:
            print("Twoje hasło jest dobre.")
            break

walidacja_pass()

#login: nazwa <20 znaków, może zawierać duże, małe litery, cyfry, @
#nie może zawierać innych znaków specjalnych
def walidacja_login():
    while True:
        login = input('Wpisz login: ')
        if len(login) > 20:
            print('Login może mieć max. 20 znaków.')
        elif re.search('[!#$%&*]', login) is not None:
            print('Hasło nie może zawierać znaków specjalnych')
        else:
            print('Login jest prawidłowy')
            break

walidacja_login()





