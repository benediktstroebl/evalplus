
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
    if len(txt) > 0:
        # if txt[-1] is not a letter
        if not txt[-1].isalpha():
            return True
        # if txt[-1] is a letter
        else:
            # if txt[-2] is a letter, and txt[-1] is not a letter
            if txt[-2].isalpha() and not txt[-1].isalpha():
                return True
            # if txt[-1] is a letter, and txt[-2] is a letter
            else:
                return False
    # if txt is empty
    else:
        return False
