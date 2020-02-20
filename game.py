import random

class Game:
    def __init__(self):
        self.player = Player(input("What is your name? "))
        self.word_list = open("words.txt", "r")
        self.render_word_list() 
    
    def render_word_list(self):
        self.word_list = self.word_list.read().split('\n')  
        # print(self.word_list)     

    def create_list_level(self):
        """Narrow word list down by length of word and then choose word from narrowed list by index, randomly"""
        words = []
        for word in self.word_list:
            if len(word) >= 4 and len(word) <= 6:
                words.append(word)
        return words
    
    def choose_random_word(self):
        list = self.create_list_level()
        random_word = random.choice(list)
        return random_word.upper()

    def convert_word_to_list(self, word):
        return list(word) 

    def display_word(self):
        """Display the word at stage of guess with underscores in place of """
        pass
    def round(self):
        


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
print(game.choose_random_word())
print(game.convert_word_to_list())
