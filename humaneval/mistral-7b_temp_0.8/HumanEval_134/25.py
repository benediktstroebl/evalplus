
def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''

    # 1. Split the string and strip the spaces
    txt_split = txt.split()
    txt_split = [item.strip() for item in txt_split]

    # 2. Loop through the list and get the last char of each element
    last_char_list = [item[-1] for item in txt_split]

    # 3. Loop through the last char list and check if the last char is
    # an alphabetical character and is not a part of a word
    for char in last_char_list:
        if char.isalpha() and not char.isupper():
            return True

    return False

