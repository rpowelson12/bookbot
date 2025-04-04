from stats import count_words, sort_char_count
import sys

def print_report(filepath, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Loop through sorted characters and print counts for alphabetical chars
    for char_dict in sorted_chars:
        char = char_dict["character"]
        # Only print if the character is alphabetical
        if char.isalpha():
            count = char_dict["count"]
            print(f"{char}: {count}")
    
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        word_count = count_words()
        sorted_chars = sort_char_count()

        print_report(sys.argv[1], word_count, sorted_chars)

main()