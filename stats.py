def get_book_text(path):
    with open(path) as f:
       file_contents = f.read()
       return file_contents
    
def count_words(text):
    items = text.split()
    return len(items)

def count_letter(text):
    letters = {}

    for s in text:
        letter = s.lower()
        if(letter in letters):
            letters[letter] += 1
        else:
            letters[letter] = 1
    
    return letters

def sort_func(letter):
    return letter["num"]
    
def sort_on(text):

    letters = count_letter(text)
    letterChar = [];

    for letter in letters:
        if(letter.isalpha()):
            letterChar.append(dict(char=letter, num=letters[letter]))
    
    letterChar.sort(reverse=True, key=sort_func)
    return letterChar

