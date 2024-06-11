# # This is my horribly written code
# def main():
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     # print(text)
#     return text
#
# def get_book_text(path):
#     with open(path) as f:
#         return f.read()
#
# def get_words():
#     text = main()
#     words = text.split()
#     # print(words)
#     count = 0
#     for word in words:
#         count += 1
#     return print(count)
#
# main()
# get_words()


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    chars_dict = get_num_chars(text)
    chars_sorted = num_chars_sorted(chars_dict) 

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print() 

    for item in chars_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    text = text.lower()
    chars = list(text)  # An alternative is to do a for loop and append to list
    # chars = "This is my text to test and count the characters.".lower()
    char_dict = {}
    for char in chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_dict(d):
    return d["num"]

def num_chars_sorted(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
        sorted_list.sort(reverse=True, key=sort_dict)
    return sorted_list

main()
