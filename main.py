import sys
from stats import count_words           # connect function count_words to main.py for use
from stats import count_characters      # connect function count_characters to main.py for use
from stats import sort_character_counts # add info

def get_book_text(filepath):
    # reads the contents of a text file and returns it as a string
    with open(filepath) as book:    # open file at destination
        return book.read()          # read contents of a file into a string

def main():
    # comments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]

    # comments
    # path_to_file = "books/frankenstein.txt"               # define filepath in directory
    text = get_book_text(path_to_file)                      # call getbook_function to read entire contents of file
    num_of_words = count_words(text)                        # count total number of words and store result in num_of_words
    char_count = count_characters(text)                     # explain
    sorted_chars = sort_character_counts(char_count)        # explain
    
    # comments
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...\n")

    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words\n")

    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():                          # Skip non-letters
            print(f"{item['char']}: {item['num']}")

    # print(f"\nFound {num_of_words} total words\n")          # print result
    
    print("============= END ===============")
    # print(char_count)  # print result



main()      # runs code

# clean this mf up