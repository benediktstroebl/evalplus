
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
    
    # convert the string into an array of characters
    txt = list(txt)
    # check if the last character is an alphabetical character
    if txt[-1].isalpha() == True:
        # check if the last character is not a part of a word
        if txt[-1].isalnum() == True:
            return False
        return True
    return False
    
