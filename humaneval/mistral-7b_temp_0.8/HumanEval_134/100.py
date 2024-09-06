
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
    #  return True if txt[-1] == ' ' or txt[-1].isalpha() else False
    #  return txt[-1] != ' ' and txt[-1].isalpha()
    #  return txt[-1] not in '0123456789' and txt[-1] not in ' ,.!?()/|-=[]{}"';'
    #  return txt[-1] not in '0123456789' and txt[-1] not in ' ,.!?()/|-=[]{}"';'
    return True if txt[-1] not in '0123456789' and txt[-1] not in ' ,.!?()/|-=[]{}"';:' else False

    # return False if not txt.strip().endswith(' ') else True
    #  return txt[-1] not in '0123456789' and txt[-1] not in ' ,.!?()/|-=[]{}"';:'
    #  return txt[-1] not in '
