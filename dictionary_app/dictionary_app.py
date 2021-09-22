from get_word_meaning import get_meaning

print("Welcome to the dictionay Application \n this application will keep running until you enter q")

while True:
    word = input('please enter a word: ').lower()
    output = get_meaning(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
   



