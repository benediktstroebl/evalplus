
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
    if len(txt) >= 1: # if text is not empty
        last_letter = txt[-1] # get last letter of a string
        if last_letter.isalpha(): # if last letter is a alpha
            if last_letter.isupper(): # if last letter is uppercase
                if txt[-2] == " ": # if there is space before the a letter
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        return False
