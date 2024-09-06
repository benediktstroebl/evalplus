
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
    
    if len(txt) == 1:
        return False
    elif len(txt) == 2:
        if not txt[-1] in string.ascii_letters:
            return False
    end = txt.rfind(' ')
    if end != -1:
        item = txt[:end]
        if not item.isalpha():
            return False
    radius = txt.rfind(' ', 0, end)
    if radius != -1:
        item = txt[end:radius]
        if not item.isalpha():
            return False
    start = txt.rfind(' ', 0, radius)
    if start != -1:
        item = txt[start:radius]
        if not item.isalpha():
            return False
    return True

