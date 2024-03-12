with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()

def letter_count(list):
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

    for word in file_contents:
        for i in word.lower():
            if i in letter:
                letter[i] += 1

    # keys = letter.keys
    # values = letter.values()
                
    str = letter.items()
    
    for i in str:
        print(f"The '{i[0]}' character was found {i[1]} times")



def main():

    word_count = 0
    for i in range(len(words)):
        word_count += 1

    letter_count(words)

    print(word_count)


main()