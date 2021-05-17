import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word():
    word = random.choice(words)

    while "-" in word and " " in word:
        word = random.choice(words)
    # print(word.upper())
    return word.upper()


def hangman():
    word = get_valid_word()
    word_letters = set(word)  # it will all character from word
    # print(word_letters)
    alphabets = set(string.ascii_uppercase)  # A to Z
    # print(alphabets)
    used_letters = set()
    lives = 7
    print("You get 10 lives at start of the game and Every wrong guess cause you -1 live")
    while len(word_letters) > 0 and lives > 0:
        # for user to know which letters are already used
        print("===========================================================================")
        print("You've used this letters: ", " " .join(used_letters))

        # when we print this word_list it wil show which number's letter is already guess and which are not
        word_list = []
        # if user's letter is in word then this for loop will run
        for letter in word:

            if letter in used_letters:
                # print(letter)
                word_list.append(letter)
            else:
                # print("-")
                word_list.append("-")
        print(lives_visual_dict[lives])
        # shortcut/one liner for word list
        # word_list[letter if letter in used_letters else "-" for letter in word]
        # print like W-RD-
        print("Current word: ", " ".join(word_list))

        user_input = input("Enter Your Letter: ").upper()
        # if user's letter is in set(set(alphabets)-set(used_letters)) then user's letter will added to used_letters
        if user_input in alphabets - used_letters:
            used_letters.add(user_input)
            # if user's letter is in word_letters then remove that letter from word_letter
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives = lives - 1
                print(
                    f"You choose {user_input} which is wrong letter. so now You have {lives} left.")
        elif user_input in used_letters:
            print("You've alredy used this letter. Try again")
        else:
            print("Invalid Input")

        # print("===========================================================================")
    # after while loop executed
    if lives == 0:
        print(lives_visual_dict[lives])
        print(f"You died... word was:{word}\nwanna play then Start again")
    else:
        print(f"You Won! You guess currect word: {word}")


if __name__ == "__main__":
    hangman()
