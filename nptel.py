import random

def choose():
    words = ['rainbow', 'computer', 'science', 'programming', 'mathematics', 'player', 'condition', 'reverse', 'water', 'boat']
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled = "".join(random.sample(word, len(word)))
    return jumbled

def thank(p1n, p2n, p1, p2):
    print(p1n, 'your score is :', p1)
    print(p2n, 'your score is :', p2)
    print("Thanks for playing")
    print("Have a nice day.")

def play():
    p1name = input("Enter your name player 1: ")
    p2name = input("Enter your name player 2: ")
    pp1 = 0
    pp2 = 0
    turn = 0
    while True:
        # computer's task
        picked_word = choose()
        # create the question 
        qn = jumble(picked_word)
        print(qn)
        # player 1
        if turn % 2 == 0:
            print(p1name, "your turn.")
            ans = input("What is on my mind? ")
            if ans == picked_word:
                pp1 += 1
                print(p1name, "has scored a point")
                print("Your score is: ", pp1)
            else:
                print("Better luck next time. I thought:", picked_word)
            c = int(input('Press 1 to continue or 0 to Quit: '))
            if c == 0:
                thank(p1name, p2name, pp1, pp2)
                break
        # player 2
        else:
            print(p2name, "your turn.")
            ans = input("What is on my mind? ")
            if ans == picked_word:
                pp2 += 1
                print(p2name, "has scored a point")
                print("Your score is: ", pp2)
            else:
                print("Better luck next time. I thought:", picked_word)
            c = int(input('Press 1 to continue or 0 to Quit: '))
            if c == 0:
                thank(p1name, p2name, pp1, pp2)
                break
        turn += 1

play()