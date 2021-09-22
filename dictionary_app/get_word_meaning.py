import json
from difflib import get_close_matches
import sys

data = json.load(open('data.json'))
def get_meaning(word):
    if word in data:
       return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
            print (get_close_matches(word, data.keys()))
            yn = input(f"Did you mean {get_close_matches(word, data.keys())[0]} instead? Enter Y if yes, or N if no: ").upper()
            if yn == "Y":
               return data[get_close_matches(word, data.keys())[0]]
            elif yn == "N":
                return "The word doesn't exist. Please double check it."
            else:
                return "We didn't understand your entry."
    elif word == 'q':
        print('You are quitting the application.....\n It was nice having you \n Good Bye and See you soon')
        sys.exit(0)
    else:
        return "You either has entered a wrong word or you can\'t be found in this dictionary"