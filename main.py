from stats import get_num_words, get_char_count
import sys



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #total_words = get_num_words(get_book_text("books/frankenstein.txt"))
    text = get_book_text(f"{sys.argv[1]}").lower()
    data = get_char_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/...{sys.argv[1]}")
    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key, value in data.most_common():
        if key.isalpha():
            print(f"{key}: {value}")
    #print(f"{total_words} words found in the document")

main()
