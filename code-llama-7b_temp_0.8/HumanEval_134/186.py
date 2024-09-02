
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
    if txt == "":
        return False
    
    last_char = txt[-1]
    try:
        last_char = ord(last_char)
        if last_char >= 65 and last_char <= 90 or last_char >= 97 and last_char <= 122:
            return False
    except TypeError:
        return False

    return True
