
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
    words = txt.split()
    if txt.endswith(words):
        for word in words:
            if word[-1].isalpha() and word[-1].isupper() and word[-1].isnumeric() == False:
                return True
    else:
        if txt[-1].isalpha() and txt[-1].isupper() and txt[-1].isdigit() == False:
            return True
    return False
