from stats import get_num_words, char_count, sort_chars
import sys

def print_report(book, words, count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for k in count:
        if k.isalpha():
            print(f"{k}: {count[k]}")



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    words = get_num_words(book)
    sorted_count = sort_chars(char_count(book))
    print_report(book, words, sorted_count)




main()
