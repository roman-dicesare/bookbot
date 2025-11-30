def number_of_words(book_text):
    word_count = 0
    split_string = book_text.split()
    for word in split_string:
        word_count += 1
    return word_count

def repeated_characters(book_text):
    lowered_text = book_text.lower()
    characters = {}
    for character in lowered_text:
        if character in characters:
            characters[character] = characters[character] + 1
        else:
            characters[character] = 1
    return characters

def sort_help(characters):
    return characters["num"]

def sort_data(characters):
    sorted_list = []
    for character, count in characters.items():
        sorted_list.append({"Char": character, "num": count})
    
    sorted_list.sort(reverse=True, key=sort_help)
    return sorted_list


