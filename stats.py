from main import get_book_text
#path = "books/frankenstein.txt"


## Import book into string

# def get_book_text(path):
#     with open(path, "r") as f:
#         frankenstein = f.read()
#         return frankenstein

## Return number of words in book

def get_num_words():
    frankenstein = get_book_text()
    words_frankenstein = frankenstein.split()
    num_words = len(words_frankenstein)
    return num_words

## Get a dictionary of characters and counts

def get_num_chars():
    frankenstein = get_book_text(path)
    frankenstein = frankenstein.lower().replace(" ","")
    list_frankenstenstein = list(frankenstein)
    char_count = {}

    for character in list_frankenstenstein:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
    return char_count

## Rturn list of dictionary where "char" is key and value is character in book,
## and key is "num" and value is the count of the character

def list_of_char_counts():
    char_count = get_num_chars()
    list_char_count = [{"char": key, "num": value } for key, value in char_count.items()]
    return list_char_count

## Return values of character count

def sort_on(list_char_count):
    return list_char_count["num"]

## Return sorted list

def sorted_list_char_count():
    list_char_count=list_of_char_counts()
    list_char_count.sort(reverse=True, key=sort_on)
    return list_char_count


sorted_list_char_count()

