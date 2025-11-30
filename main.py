from stats import number_of_words,repeated_characters,sort_data
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) == 2:
        book_string = get_book_text(sys.argv[1])
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    new_dict = repeated_characters(book_string)

    sorted_list = sort_data(new_dict)

    # boilerplate

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words(book_string)} total words")
    print("--------- Character Count -------")
    for data in sorted_list:
        if data["Char"].isalpha():
            print(f"{data["Char"]}: {data["num"]}")
    print("============= END ===============")

main()
