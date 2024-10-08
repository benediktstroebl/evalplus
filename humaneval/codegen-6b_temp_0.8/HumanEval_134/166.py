
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
    if (txt[-1] in alphabet) and (not txt[-1].isalpha()) and (txt[-2] != ' '):
        return True
    elif txt[-1] in alphabet and not txt[-1].isalpha():
        return True
    elif txt[-1] not in alphabet and txt[-1] != ' ':
        return False
    elif txt[-1] == ' ' and txt[-2] != ' ':
        return False
    elif txt[-1] == ' ' and txt[-2] == ' ':
        return True
    else:
        return False


alphabet = 'abcdefghijklmnopqrstuvwxyz'

import sys # should make this an option
