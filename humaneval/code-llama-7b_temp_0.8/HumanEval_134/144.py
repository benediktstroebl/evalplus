
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

    # METHOD 1: Lists
    # words = txt.split()

    # if words[-1][-1].isalpha() and words[-1][-1] != words[-1][-2]:
    #     return True
    # return False

    # METHOD 2: Regex
    # import re
    # if re.match(r"[a-z]$", txt):
    #     return True
    # return False

    # METHOD 3: String method
    return txt[-1].isalpha() and txt.rsplit(None, 1)[-1][-1] != txt.rsplit(None, 1)[-1][-2]
