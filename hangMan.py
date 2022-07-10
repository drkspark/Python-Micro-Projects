import random

print("H A N G M A N  # 8 attempts\n")

words = ["python", "java", "swift", "javascript"]
wins = 0
loss = 0

def play_game():
    ans = random.choice(words)

    st = set(ans)
    usr_guess = "-"*len(ans)
    usr_guess = list(usr_guess)
    num = 7

    used = set()

    found = False

    while num != -1:
        print("".join(usr_guess))
        
        ch = input("Input a letter:")
        
        if len(ch) != 1 or ch.isspace():
            print("Please, input a single letter.")
            continue
        if not ch.isalpha() or not ch.islower():
            print("Please, enter a lowercase letter from the English alphabet.")
            continue
        if ch in used:
            print("You've already guessed this letter.")
            continue        
        
        used.add(ch)
        
        if ch in st:
            st.discard(ch)
            for i in range(len(ans)):
                if ans[i] == ch:
                    usr_guess[i] = ch
            if "".join(usr_guess) == ans:
                found = True
                break
            
            continue    
        
        elif ch in usr_guess:
            print("No improvements.")
        
        else:
            print("That letter doesn't appear in the word.")
        
        if "".join(usr_guess) == ans:
            found = True
            break
        
        print('\n')
        num -= 1
        

    if found:
        print("You guessed the word {}!".format(ans))
        print("You survived!")
    else:
        print("You lost!")
    
    return found



while True:
    op = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if op == "play":
        c = play_game() 
        if c:
            wins += 1
        else:
            loss += 1
            
    elif op == "results":
        print("You won: {} times.".format(wins))
        print("You lost: {} times.".format(loss))
    elif op == "exit":
        break
    