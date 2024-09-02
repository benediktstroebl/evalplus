
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
    # your code here
    # can you use regex for this problem?

    # check if the last character is a word
    if txt[-1].isspace():
        return False

    # check if the last character is a letter
    if not any(c.isalpha() and not c.isspace() for c in txt[:-1]):
        return False

    return True