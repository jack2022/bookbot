from stats import get_num_words, sorted_list_char_count, get_book_text, get_num_chars, list_of_char_counts
import sys

if len(sys.argv) < 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)

def main(path, num_words, sorted_list):
    text = "============ BOOKBOT ============"
    text += "\nAnalyzing book found at {path}"
    text += "\n----------- Word Count ----------"
    text += f"\n Found {num_words} total words"
    text += "\n--------- Character Count -------"
    print(text)
    for item in sorted_list:
        char = item['char']
        num = item['num']
        print(f"\n{char}: {num}")

path = sys.argv[1]

frankenstein = get_book_text(path)
num_words = get_num_words(frankenstein)
char_count = get_num_chars(frankenstein)
list_char_count = list_of_char_counts(char_count)
sorted_list = sorted_list_char_count(list_char_count)



main(path, num_words, sorted_list)
