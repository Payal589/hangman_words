import hangman_words
import random
lives=6
chosen_word=random.choice(hangman_words.word_list)
print(chosen_word)
word_length=len(chosen_word)
space=""
for dash in range(word_length ):
    space+= "_"
print(space)
list1=[]
list2=[]
continue_game ="true"
while continue_game == "true":
    correct_word=""
    guess_word=input("guess the letter for word?\n ")
    if guess_word in list2:
        print("you already guessed it ")


    elif guess_word not in chosen_word:
        list2.append(guess_word)
        lives-=1
        print(f"*********  {lives} chances are left to you *********")
    else:
        list2.append(guess_word)
        for letter in chosen_word :
            if guess_word == letter:
                correct_word+=guess_word
                list1.append(letter)
            elif letter in list1:
                correct_word+=letter
            else:
                correct_word+="_"
        print(correct_word)

    if lives>0:
        continue_game="true"
        if correct_word == chosen_word:
            continue_game="false"
            print("************  congratulation! you win.  *********")

    else:
        continue_game="false"
        print("oops! you loose")
        print(f"The word you need to guessed is {chosen_word}")


