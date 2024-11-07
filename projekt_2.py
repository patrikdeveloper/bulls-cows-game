"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Patrik Hlaváč
email: pathlavac@seznam.cz
discord: patrik_py
"""

import time
import random

def initiate_intro():
    """
    Zobrazí úvodní zprávu pro hráče.
    
    Funkce vytiskne pozdrav a úvodní instrukce pro hru Bulls and Cows.
    """
    print("Hi there!")
    print("-" * 47)
    print("I've generated a random 4-digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)

def generate_random_number():
    """
    Vygeneruje náhodné 4místné číslo pro hru.

    Funkce náhodně vybere čtyři unikátní číslice z rozmezí 1-9 a vrátí je ve formě řetězce.
    
    Nikdy nevygeneruje 0.
    
    Returns:
        str: Náhodně vygenerované 4místné číslo jako řetězec.
    """
    gener_number = random.sample(range(1, 10), 4)
    number = "".join(map(str, gener_number))
    return number

def get_user_guess(users_attempt, invalid_count):
    """
    Získá a ověří vstup od uživatele.

    Funkce kontroluje, zda je vstup 4místné číslo, zda neobsahuje opakující se číslice a nezačíná nulou.
    Pokud vstup není platný, uživatel je znovu požádán o zadání. Počet neplatných vstupů je zaznamenán.

    Args:
        users_attempt (str): Vstup od uživatele, který se má ověřit.
        invalid_count (int): Počet neplatných pokusů uživatele.

    Returns:
        tuple: Ověřený vstup uživatele (str) a aktualizovaný počet neplatných vstupů (int).
    """
    while len(users_attempt) != 4 or not users_attempt.isdigit() or len(set(users_attempt)) != 4 or users_attempt.startswith("0"):
        print("Invalid input. Please enter 4 unique digits.")
        invalid_count += 1
        print("-" * 47)
        users_attempt = input(">>>").strip()
    return users_attempt, invalid_count

def calculate_bulls_and_cows(secret_num, users_attempt):
    """
    Spočítá počet bulls a cows pro daný pokus uživatele.

    Funkce porovná uživatelův pokus s tajným číslem a vrátí počet bulls (správně umístěné číslice) 
    a cows (číslice, které jsou obsaženy ve správném čísle, ale jsou na nesprávném místě).

    Args:
        secret_num (str): Tajné číslo, které má uživatel uhodnout.
        users_attempt (str): Pokus uživatele.

    Returns:
        tuple: Počet bulls (int) a cows (int).
    """
    bulls = sum(1 for i in range(len(secret_num)) if secret_num[i] == users_attempt[i])
    cows = sum(1 for j in users_attempt if j in secret_num) - bulls
    return bulls, cows

def play_bulls_and_cows():
    """
    Spustí hru Bulls and Cows.

    Funkce provádí veškerou logiku hry, od inicializace až po získání vstupu od uživatele, 
    výpočet výsledků a zobrazení výsledku po každém pokusu. Hra končí, jakmile uživatel uhodne tajné číslo.
    """
    initiate_intro()
    attempt = 0
    bulls = 0
    invalid_count = 0
    secret_num = generate_random_number()  # Náhodně vygenerované číslo
    # Požadavek na první vstup od uživatele
    users_attempt = input("Enter a number:").strip()
    users_attempt, invalid_count = get_user_guess(users_attempt, invalid_count)
    
    while bulls != 4:
        # Výpočet bulls a cows pro současný pokus
        bulls, cows = calculate_bulls_and_cows(secret_num, users_attempt)
        attempt += 1
        
        bull_text = "bull" if bulls == 1 else "bulls"
        cow_text = "cow" if cows == 1 else "cows"
        print(f"{bulls} {bull_text}, {cows} {cow_text}")
        print("-" * 47)
        
        # Pokud není uhádnuto, získáme nový vstup bez opakované výzvy
        if bulls != 4:
            users_attempt = input(">>>").strip()
            users_attempt, invalid_count = get_user_guess(users_attempt, invalid_count)  # Aktualizace počtu neplatných vstupů

    # Výsledná zpráva o počtu pokusů a správném uhádnutí
    guess_text = "guess!" if attempt == 1 else "guesses!"
    print(f"Correct, you've guessed the right number\nin {attempt} {guess_text}")
    print("-" * 47)
    print("That's amazing")
    print("-" * 47)
    print(f"Number of invalid inputs: {invalid_count}")
    print("-" * 47)

def main():
    """
    Hlavní funkce pro spuštění hry Bulls and Cows s měřením času.

    Funkce spustí hru, změří celkový čas potřebný k uhádnutí čísla a zobrazí tento čas v minutách a sekundách.
    """
    start_time = time.time()
    play_bulls_and_cows()
    end_time = time.time()
    played_time = end_time - start_time
    round_played_time = round(played_time)
    minutes, seconds = divmod(round_played_time, 60)
    print("You have guessed the secret number\nafter", minutes, "minutes", "and", seconds, "seconds.")    

if __name__ == "__main__":
    main()
