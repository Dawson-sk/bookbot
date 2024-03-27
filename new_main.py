import os

path = 'books'
os.chdir(path)

def read_text_file(file_path):
    with open(file_path, 'r') as fd:
        file_contents = fd.read()
        words = file_contents.split()
    return file_contents, words
    
def letter_count(file_contents):
    letter = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }       
    seen = []
    list = []

    for word in file_contents:
        for i in word.lower():
            if i in letter:
                letter[i] += 1

    for i in range(len(letter)):
        key, high = "", 0
        for k,v in letter.items():
            if v > high and k not in seen:
                key = k
                high = v

        seen.append(key)
        list.append(f"The '{key}' character was found {high} times")

    return list

def make_report(wcount, letters):
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{wcount} words found in the document\n\n")

    for i in letters:
        print(i)

def main():
    try:
        dirs = []
        books = []
        for file in os.listdir():
            if file.endswith(".txt"):
                file_path = f"{file}"
                books.append(f"{file}")
                dirs.append(file_path)
    except Exception as err:
        return err


    while True:
        try:
            print(f'\n\n {books}')
            put = input("\n    Please select book to report. \n         Press Ctrl+C to exit. \n")
            select = books.index(f'{put}')

            file_contents, words = read_text_file(dirs[select])

            word_count = 0
            for i in range(len(words)):
                word_count += 1

            l = letter_count(words)
            make_report(word_count, l)
        except Exception as err:
            print('\n\n   ----- Book not found -----')



main()

