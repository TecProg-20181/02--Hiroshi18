import random
import string

WORDLIST_FILENAME = "words.txt"

class Word:

    def __init__(self):
        self.word = ''
        self.lettersGuessed = []

    def loadFile(self):
        self.inFile = open(WORDLIST_FILENAME, 'r', 0)
        return self.inFile

    def loadWords(self):
        print "Loading word list from file..."
        # inFile: file
        self.inFile = open(WORDLIST_FILENAME, 'r', 0)
        # line: string
        line = self.inFile.readline()
        # wordlist: list of strings
        wordlist = string.split(line)
        print "  ", len(wordlist), "words loaded."
        self.word = random.choice(wordlist).lower()

    def isWordGuessed(self):
        for letter in self.word:
            if letter in self.lettersGuessed:
                pass
            else:
                return False
        return True

    def getGuessedWord(self):
        guessed = ''
        for letter in self.word:
            if letter in self.lettersGuessed:
                guessed = guessed + letter
            else:
                guessed = guessed + '_ '
        return guessed

    def getAvailableLetters(self):
        import string
        available = string.ascii_lowercase
        for letter in available:
            if letter in self.lettersGuessed:
                available = available.replace(letter, '')
        return available
    
    def differentLetters(self):
        return len(set(self.word))

class Hangman:
    def __init__(self):
        self.guesses = 8
        self.secretWord = Word()
        self.secretWord.loadWords()

    def WelcomeMessage(self):
        print 'Welcome to the game, Hangam!'
        print 'I am thinking of a word that is', len(self.secretWord.word), ' letters long.'
        print 'Has', self.secretWord.differentLetters(), 'different letters'
        print '-------------'
    
    def wordTest(self):
        while self.secretWord.differentLetters() > self.guesses:
            print 'We have different letters is greater than the number of attempts\nNew Word?\ny- yes\nn- no'
            input = raw_input()
            if input == 'y':
                self.secretWord.loadWords()
            else:
                break

    def gameStart(self):
        while  self.secretWord.isWordGuessed() == False and self.guesses > 0:
            print 'You have ', self.guesses, 'self.guesses left.'
            available = self.secretWord.getAvailableLetters()
            print 'Available letters', available
            letter = raw_input('Please guess a letter: ')

            if letter in self.secretWord.lettersGuessed:
                guessed = self.secretWord.getGuessedWord()
                print 'Oops! You have already guessed that letter: ', guessed
            elif letter in self.secretWord.word:
                self.secretWord.lettersGuessed.append(letter)
                guessed = self.secretWord.getGuessedWord()
                print 'Good Guess: ', guessed
            else:
                self.guesses -= 1
                self.secretWord.lettersGuessed.append(letter)
                guessed = self.secretWord.getGuessedWord()
                print 'Oops! That letter is not in my word: ', guessed            
            print '------------'
        else:
            if self.secretWord.isWordGuessed():
                print 'Congratulations, you won!'
            else:
                print 'Sorry, you ran out of guesses. The word was ', self.secretWord.word, '.'

    def main(self):
        self.WelcomeMessage()
        self.wordTest()
        self.gameStart()

if __name__ == '__main__':
    game = Hangman()
    game.main()