
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
    #first, check if the string is empty
    if len(txt) == 0:
        return False
    #if not empty, check if the last character is a letter and is not part of a word
    elif txt[-1].isalpha():
        if len(txt.split()) == 1:
            return True
        else:
            return False
    else:
        return False
