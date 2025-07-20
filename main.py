import sys

# imports functions from stats.py
from stats import get_num_words
from stats import char_in_text
from stats import sort_chars_by_num


# takes a filepath to .txt file as a str and return contents as a str 
def get_book_text(filepath):
    with open(filepath) as f:
        text_file = f.read()
    return text_file

# #### main ####
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    chars = char_in_text(text)
    sorted_chars = sort_chars_by_num(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")
    print("============= END ===============")

main()