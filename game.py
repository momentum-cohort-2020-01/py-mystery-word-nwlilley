import random

class Game:
    def __init__(self):
        self.player = Player(input("What is your name? ").upper())
        self.word_list = open("words.txt", "r")
        self.render_word_list()
        self.round()
    
    def render_word_list(self):
        self.word_list = self.word_list.read().split('\n')  

    def choose_level(self):
        greeting = f'Hello, {self.player.name}. What level of difficulty would you like to play?\nChoose \'(e)asy\', \'(n)ormal\', or \'(h)ard\'>>> '
        valid_level_entries = ('E','N', 'H', 'EASY', 'NORMAL', 'HARD')
        choice = input(greeting)
        while choice.upper() not in valid_level_entries:
            print("\nNot a valid entry. Please try again\n")
            choice = input(greeting)
        return choice

    def create_list_level(self, level_of_difficulty):
        """Narrow word list down by length of word and then choose word from narrowed list by index, randomly"""
        words = []
        for word in self.word_list:
            if level_of_difficulty == 'EASY' or level_of_difficulty == 'E':
                if len(word) >= 4 and len(word) < 6:
                    words.append(word)
            elif level_of_difficulty == 'NORMAL' or level_of_difficulty == 'N':
                if len(word) >= 6 and len(word) < 8:
                    words.append(word)    
            elif level_of_difficulty == 'HARD' or level_of_difficulty == 'H':
                if len(word) >= 8:
                    words.append(word)
        return words
                     
    def choose_random_word(self, level_of_difficulty):
        list = self.create_list_level(level_of_difficulty)
        random_word = random.choice(list)
        return random_word.upper()
    

    def convert_word_to_list(self, word):
        return list(word) 

    def display_blank_word(self, word):
        """Display the word at stage of guess with underscores in place of letters """
        display = '\n\n' + len(word) * "_ " + '\n'
        print(display)

    def create_blank_list(self, word):
        return list(len(word) * '_')

    def display_guesses_remaining(self):
        print(f'\nGuesses remaining: {self.player.guesses}')

    def check_guess(self, guess, word, word_in_progress):
        word_to_check = self.convert_word_to_list(word)
        letter_index = []
        idx = -1
        if guess in word_to_check:
            for char in word:
                idx += 1
                if guess == char:
                    letter_index.append(idx)
                    for i in letter_index:
                        word_in_progress[i] = guess           
            return word_in_progress 
        else:
            print(f'\n{guess} is not in the Mystery Word.')
            self.player.guesses -= 1
            return word_in_progress
                    
    def start_new_round(self):
        play = input("\nWould you like to play again? \n").upper()
        if play == 'YES' or play =='Y':
            self.player.guesses = 8
            self.round()
        
    def show_end_message(self, message):
        message_decoration = '\n' + len(message) * '+' + '\n'
        print(f'{message_decoration}{message}{message_decoration}')
    
    def show_winner(self):
        self.show_end_message('YOU ARE THE WINNER!!!')
    
    def show_loser(self, mystery_word):
        self.show_end_message('GAME OVER')
        print(f'The Mystery Word was {mystery_word}')


    def round(self):
        level_choice = self.choose_level().upper()
        mystery_word = self.choose_random_word(level_choice)
        skeleton_word = self.create_blank_list(mystery_word)
        checked_guess = []
        # print(mystery_word)
        self.display_blank_word(mystery_word)
        while self.player.guesses > 0:
            guess = input("Please enter a letter: ").upper()
            if guess in checked_guess:
                print(f'\nYou already entered \'{guess}\'. Try again.')
            elif len(guess) < 1 or len(guess) > 1:
                print(f'\nNot a valid entry. Try again.')
            else:
                update = self.check_guess(guess, mystery_word, skeleton_word)
                checked_guess.append(guess)
                print("\n\n" + " ".join(update) + "\n")
                self.display_guesses_remaining()
                if "_" not in update:
                    self.show_winner()
                    self.start_new_round()
                    break
        else:
            self.show_loser(mystery_word)
            self.start_new_round()


class Player:
    def __init__(self, name):
        self.name = name
        self.guesses = 8
    
    def __str__(self):
        return f"{self.name}"

game = Game()

