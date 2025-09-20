from collections import Counter

def get_num_words(book):
    return len(book.split())

def get_char_count(text):
    return Counter(text.lower())