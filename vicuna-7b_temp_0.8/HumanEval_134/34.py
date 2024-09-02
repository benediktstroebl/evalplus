
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
    is_alphabet = True
    if last_char == ' ':
        last_char = txt[-2]
        is_alphabet = False
    for i in range(len(txt) - 2):
        if txt[i] == ' ' and txt[i+1] == ' ':
            is_alphabet = True
            break
    return not is_alphabet
