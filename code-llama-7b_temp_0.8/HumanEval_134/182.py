
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
    # Create list from text
    txt = list(txt)
    
    # Take last element from list
    last_char = txt[-1]
    
    # Check if last character is alphabetic and not part of word
    if last_char.isalpha() and last_char != " ":
        return True
    else:
        return False

