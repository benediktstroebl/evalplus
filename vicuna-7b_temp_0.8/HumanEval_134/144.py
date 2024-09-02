
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
    # if txt is empty, return False
    if not txt:
        return False
    
    # if last char is a space, return True
    if txt[-1] == ' ':
        return True
    
    # if txt has only one char and that is a letter, return True
    if len(txt) == 1 and re.match(r'^[a-zA-Z]$', txt[0]):
        return True

    # check if txt ends with a word
    if re.match(r'^[a-zA-Z\s]+$', txt[-1:]):
        return False

    return True
