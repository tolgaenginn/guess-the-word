import random as rd

english_words = [
    "time", "year", "people", "way", "day", "man", "thing", "woman", "life", "child",
    "world", "school", "state", "family", "student", "group", "country", "problem", "hand", "part",
    "place", "case", "week", "company", "system", "program", "question", "work", "government", "number",
    "night", "point", "home", "water", "room", "mother", "area", "money", "story", "fact",
    "month", "lot", "right", "study", "book", "eye", "job", "word", "business", "issue",
    "side", "kind", "head", "house", "service", "friend", "father", "power", "hour", "game",
    "line", "end", "member", "law", "car", "city", "community", "name", "president", "team",
    "minute", "idea", "kid", "body", "information", "back", "parent", "face", "others", "level",
    "office", "door", "health", "person", "art", "war", "history", "party", "result", "change",
    "morning", "reason", "research", "girl", "guy", "moment", "air", "teacher", "force", "education"
    ]


def guess_the_word():
    comp_guess = rd.choice(english_words)
    correct_guesses = set()
    wrong_guesses = set()
    lives = 10
    print("Guess the random word!")

    while lives > 0 and correct_guesses != set(comp_guess):
        #prints out the letters that are correctly guessed and the ones that are missing
        for i in range(len(comp_guess)):
            if comp_guess[i] in correct_guesses:
                print(comp_guess[i], end=' ')
            else:
                print("_", end=' ')
        print(f"You have {lives} lives left")

        user_guess = input("Your guess is: ").lower()
        #exceptional cases
        if user_guess in correct_guesses or user_guess in wrong_guesses:
            print("You already used this letter")
        elif len(user_guess) > 1:
            print("Invaid input")

        #valid cases
        elif user_guess in comp_guess:
            print("Correct guess!")
            correct_guesses.add(user_guess)
        else:
            print("Wrong guess!")
            wrong_guesses.add(user_guess)
            lives -= 1

    #after the while loop, user either wins or loses
    if lives == 0:
        print(f"You lost. The correct word was: '{comp_guess}'")
    else:
        print(f"You guessed the word '{comp_guess}' correctly!")



if __name__ == '__main__':
    guess_the_word()










