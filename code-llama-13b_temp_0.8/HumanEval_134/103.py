
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

    # String length check
    if len(txt) == 0:
        return False
    
    # Find all words in string
    words = txt.split(" ")

    # Find last word in string
    last_word = words[-1]

    # Find last char in string
    last_char = txt[-1]

    # Check if last char is a letter
    if last_char.isalpha() == False:
        return False

    # Check if last char is a part of last word
    if last_char in last_word:
        return False
    
    return True

    
