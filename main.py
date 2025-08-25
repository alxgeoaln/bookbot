import sys

from stats import get_book_text
from stats import count_words
from stats import sort_on


def main():
    sys_args = sys.argv

    if(len(sys_args) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys_args[1])
    print(f"Found {count_words(book_text)} total words")

    letters = sort_on(book_text)

    for char in letters:
        print(f"{char["char"]}: {char["num"]}")

main()