###Cant figure out how to organize my code here.



from stats import get_num_words, sorted_list_char_count
import sys
path = "books/frankenstein.txt"

def get_book_text(path):
    with open(path, "r") as f:
        frankenstein = f.read()
        return frankenstein

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 main.py <path_to_book>")
    else:
        num_of_words = get_num_words()
        sorted_list = sorted_list_char_count()
        text = "============ BOOKBOT ============"
        text += "\nAnalyzing book found at books/frankenstein.txt..."
        text += "\n----------- Word Count ----------"
        text += f"\n Found {num_of_words} total words"
        text += "\n--------- Character Count -------"
        print(text)
        for item in sorted_list:
                    char = item['char']
                    num = item['num']
                    print(f"\n{char}: {num}")




main()
