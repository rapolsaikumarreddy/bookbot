def main():
    path = "books/frankenstein.txt"
    content = read_file(path)
    count = count_words(content)
    char_dict = get_num_char(content)
    list_sorted = convert(char_dict)
    get_word_report(count, list_sorted)

def read_file(path):
    with open(path) as f:
        return f.read()

def count_words(content):
    return len(content.split())

def get_num_char(content):
    char_dict = {}
    for str in content:
        lowered_str = str.lower()
        if lowered_str in char_dict:
            char_dict[lowered_str] += 1
        else:
            char_dict[lowered_str] = 1
    return char_dict

def convert(char_dict):
    char_list = []
    for char in char_dict:
        if char.isalpha():
            char_list.append({"char": char, "num": char_dict[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(dict):
    return dict["num"]

def get_word_report(count, list_sorted):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    print()
    for dict in list_sorted:
        print(f"The '{dict['char']}' character was found {dict['num']} times")
    print("--- End report ---")

main()