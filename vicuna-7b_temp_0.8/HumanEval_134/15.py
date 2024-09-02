
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
    last_char = txt[-1]
    is_alphabetical = False
    is_last_char_not_part_of_word = False

    if txt[-1].isalpha():
        is_alphabetical = True
    else:
        is_last_char_not_part_of_word = True

    if txt[-1] not in txt.split():
        is_alphabetical = True

    return is_alphabetical and not is_last_char_not_part_of_word
