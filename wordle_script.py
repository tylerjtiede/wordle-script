from english_words import english_words_set
import random

colorList = [0,0,0,0,0]
fiveLetter = []

# create list of all 5 letter words

for word in english_words_set:
    if "'" not in word:
        if len(word) == 5:
            word = word.lower()
            fiveLetter.append(word)

# color code:
# 0 = grey
# 1 = yellow
# 2 = green

for _ in range(5): # loop through whole thing 5 times (for each guess)
    guess = input("Type guess used:").lower()
    while True:
        if len(guess) == 5:
            break
        else:
            print("Choose a 5 letter word!\n")
            guess = input("Type guess used:").lower()

    i = 0
    while i < 5:
        color = str(input(f'What color was letter {i+1}?')).lower()
        if color == "gray" or color == "grey":
            colorList[i] = 0
            i += 1
        elif color == 'yellow':
            colorList[i] = 1
            i += 1
        elif color == 'green':
            colorList[i] = 2
            i += 1
        else:
            print("Wrong Color Input")
            continue
    
    #debug
    #fiveLetter = ['cheat']

    for n, word in enumerate(fiveLetter):
        # must check if the word is in the list since it might be taken out in an earlier step

        # if letter is green or yellow, remove all words that don't have that letter
        for i in range(5):
            if word != '':
                if (colorList[i] == 2 or colorList[i] == 1) and guess[i] not in word:
                    fiveLetter[n] = ''
        # if letter is grey, remove all words that have that letter in that position
        for i in range(5):
            if word != '':
                if colorList[i] == 0 and guess[i] == word[i]:
                    fiveLetter[n] = ''
        # if letter is grey, remove all words that have that letter (also check duplicates)
        for i in range(5):
            if word != '':
                if colorList[i] == 0 and guess[i] in word and guess.count(guess[i]) == 1:
                    fiveLetter[n] = ''
                elif colorList[i] == 0 and guess[i] in word and guess.count(guess[i]) > 1:
                    greyCount = 0
                    for j in range(5):
                        if guess[i] == guess[j] and colorList[j] == 0:
                            greyCount += 1
                    if greyCount == guess.count(guess[i]):
                        fiveLetter[n] = ''


        # if letter is green, and word doesn't have that letter in that position, remove word
        for i in range(5):
            if word != '':
                if colorList[i] == 2 and guess[i] != word[i]:
                    fiveLetter[n] = ''
        # if letter is yellow, and word has that letter in that position, remove word
        for i in range(5):
            if word != '':
                if colorList[i] == 1 and word[i] == guess[i]:
                    fiveLetter[n] = ''



    fiveLetter = list(filter(None, fiveLetter))

    print(fiveLetter)

    choose = random.randrange(0,len(fiveLetter))

    print(f'Next guess randomly chosen: {fiveLetter[choose]}')
