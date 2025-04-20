import sys
from stats import (
    count_words, 
    count_characters, 
    sort_dictionary
)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]

    frankenstein_text = get_book_text(path_to_book)
    num_words = count_words(frankenstein_text)
    num_characters_dict = count_characters(frankenstein_text)
    num_characters_sorted_list = sort_dictionary(num_characters_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character_list_item in num_characters_sorted_list:
        if character_list_item["character"].isalpha():
            print(f"{character_list_item['character']}: {character_list_item['character_count']}")

    print("============= END ===============")

main()