import requests
import sys

from config import config

class OffensiveWordChecker:
    '''
    Class that provides functionality and data storage for checking whether
    words are offensive or not.

    Uses the Merriam Webster Collegiate Dictionary API with Audio. The MW API 
    is here: https://dictionaryapi.com/.
    '''
    def __init__(self):
        self.api_key = config['api_key']
        # Dictionary store to remove repeated calls to API
        self.dictionary = {}

    def run_file(self, filepath):
        '''
        Runs the word checker in batch mode:
        Loops through the given file, printing out whether the words contained
        are offensive or not. Words are assumed to be one per line
        
        Params:
            filepath (str): path to txt file containing list of words
        '''
        with open(filepath, 'r') as f:
            for line in f:
                print(f'{line}: {self.run_word(line)}')

    def run_repl(self):
        '''
        Runs the word checker in interactive mode:
        Prompts the user for words from the command line and reports back
        whether the word is offensive or not.

        Keyboard Interrupts (Ctrl-C, Ctrl-D) exit interactive mode.
        '''
        while True:
            try:
                print('Enter a word to check if it is offensive:')
                word = input('> ')
                print(f'{word}: {self.run_word(word)}')
            except (KeyboardInterrupt, EOFError) as e:
                print('\nExiting...')
                break

    def run_word(self, word):
        '''
        Takes a word argument and returns whether it is offensive or not.
        Checks against the stored dictionary first in order to minimize
        API calls.

        Params:
            word (str): a string representing a word to be checked for 
                        offensiveness
        Returns:
            boolean:    True if the word is offensive, False otherwise
        '''
        if word in self.dictionary:
            return self.dictionary[word]

        res_json = self.get_api_request_json(word)

        if res_json:
            self.dictionary[word] = res_json['meta']['offensive']
            return res_json['meta']['offensive']
        else:
            return False

    def get_api_request_json(self, word):
        '''
        Makes a call to the Merriam Webster dictionary API. Returns a 
        dictionary with the word's information if the call succeeds. 
        Otherwise, returns an empty dict. Example call:
        https://www.dictionaryapi.com/api/v3/references/collegiate/json/voluminous?key=your-api-key

        Params:
            word (str): a string representing a word to be used in API
                        call
        Returns:
            dict:       A dictionary that contains the word's information
                        if the API call was successful or empty otherwise 
        '''
        res = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={self.api_key}")
        res_json = res.json()
        if res_json and type(res_json[0]) == type(dict()):
            return res_json[0]
        else:
            return dict()



if __name__ == '__main__':
    owc = OffensiveWordChecker()
    if len(sys.argv) > 2:
        print('Usage: python3 check_offensive_words.py <filepath>')
        sys.exit(1)
    elif len(sys.argv) == 2:
        owc.run_file(sys.argv[1])
    else:
        owc.run_repl()
    