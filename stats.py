import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words():
    words = len(get_book_text(sys.argv[1]).split())
    return words

def count_chars():
    chars = get_book_text(sys.argv[1]).lower()

    char_count = {}

    for char in chars:    
        if char in char_count:
            char_count[char] += 1
        else: 
            char_count[char] = 1
    return(char_count)

def sort_char_count():
    dict = count_chars()
    chars_list = []

    for char, count in dict.items():
        char_dict = {"character": char, "count": count}
        chars_list.append(char_dict)

    def sort_on(dict):
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list
