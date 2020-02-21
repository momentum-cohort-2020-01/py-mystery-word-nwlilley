import random

class Game:
    def __init__(self):
        self.player = Player(input("What is your name? "))
        self.word_list = open("words.txt", "r")
        self.render_word_list() 
    
    def render_word_list(self):
        self.word_list = self.word_list.read().split('\n')  

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
            else:
                print("do something with level choice error")
                break
        return words
                
    
    def choose_random_word(self, level_of_difficulty):
        list = self.create_list_level(level_of_difficulty)
        random_word = random.choice(list)
        return random_word.upper()

    def convert_word_to_list(self, word):
        return list(word) 

    def display_blank_word(self, word):
        """Display the word at stage of guess with underscores in place of """
        display = len(word) * "_ " 
        print(display)

    def create_blank_list(self, word):
        return list(len(word) * '_')

    
    def check_guess(self, word, empty_word):
        guess = input("Please enter a letter: ").upper()
        word_to_check = self.convert_word_to_list(word)
        print(word)
        letter_index = []
        idx = -1
        if guess in word_to_check:
            for char in word:
                idx += 1
                if guess == char:
                    letter_index.append(idx)
                    for i in letter_index:
                        empty_word[i] = guess           
            print("guess is correct")
            # print(letter_index)
            print(empty_word)
        

        
        else:
            print("guess is incorrect")
            self.player.guesses -= 1
            print(f'Guesses remaining: {self.player.guesses}')
        
    def start_new_round(self):
        play = input("Would you like to play again? ").upper()
        if play == 'YES' or play =='Y':
            self.player.guesses = 8
            self.round()
        
    def round(self):
        level_choice = input(f'Hello, {self.player.name}. What level of difficulty would you like to play?\nChoose \'(e)asy\', \'(n)ormal\', or \'(h)ard\'>>> ').upper()
        mystery_word = self.choose_random_word(level_choice)
        skeleton_word = self.create_blank_list(mystery_word)
        print(mystery_word)
        self.display_blank_word(mystery_word)
        while self.player.guesses > 0:
            self.check_guess(mystery_word, skeleton_word )
            
        else:
            print("\n+++++++++\nGAME OVER\n+++++++++\n")
            self.start_new_round()

        #Get first guess
        pass



class Player:
    def __init__(self, name):
        self.name = name
        self.guesses = 8
    
    def __str__(self):
        return f"{self.name}"

    def remove_guesses(self):
        pass


game = Game()
# print(game.word_list())
game.round()
