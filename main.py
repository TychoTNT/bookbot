def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report for {book_path} ---")
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    print("")
    print("")
    sorted_letter_list (text)
    print ("--- End Report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def lower_case(my_string):
    lowered_string = my_string.lower()
    return (lowered_string)

def count_letters(my_string):
    lowered_string = lower_case(my_string)
    letter_dict = {}
    for char in lowered_string:
        if char.isalpha():
            if char in letter_dict:
                letter_dict[char]+=1
            else:
                letter_dict[char]=1
    return (letter_dict)

def dict_to_dict_list(dict):
    dict_list=[]
    for item in dict:
        dict_list.append({"letter": item, "count": dict[item]})
    return (dict_list)

def sort_on(dict):
    return dict["count"]

def sorted_letter_list (text):
    letter_dict = count_letters(text)
    #print (letter_dict)
    letter_dict_list=dict_to_dict_list(letter_dict)
    letter_dict_list.sort(reverse=True, key=sort_on)
    #print (letter_dict_list)
    for dict in letter_dict_list:
        print(f"The '{dict["letter"]}' character was found {dict["count"]} times")
    return()


main()