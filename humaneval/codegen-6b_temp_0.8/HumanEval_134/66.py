
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
    txt = str(txt) # convert to string, to use break method
    if txt[-1] == " ": # check if last character is a space
        return False
    elif txt[-1] == ".": # check if last character is a dot
        return False
    elif txt[-1] == "'": # check if last character is a apostrophe
        return False
    elif txt[-1] == "!": # check if last character is a exclamation mark
        return False
    elif txt[-1] == "?": # check if last character is a question mark
        return False
    elif not txt[-1].isalpha(): # check if last character is a letter
        return True
    else:
        return False
