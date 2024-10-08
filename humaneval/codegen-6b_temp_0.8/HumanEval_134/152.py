
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
    if len(txt) < 2:
        return False
    last_char = txt[-1]
    if not last_char.isalpha():
        return True
    if txt[-2].isalpha():
        return False
    if txt[-2].isnumeric():
        return False
    if txt[-2] == " ":
        return False
    if last_char == " ":
        return False
    return True

