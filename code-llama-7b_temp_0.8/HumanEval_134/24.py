
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
    if txt == '':
        return False
    elif txt[-1] == ' ':
        return False
    elif txt[-1] == '.' or txt[-1] == '!' or txt[-1] == '?':
        return False
    elif ' ' not in txt:
        return False
    elif len(txt) == 1:
        return False
    else:
        last_char = txt[-2]
        if last_char == ' ':
            return False
        elif last_char == '.' or last_char == '!' or last_char == '?':
            return False
        elif ' ' not in txt:
            return False
        else:
            return True
