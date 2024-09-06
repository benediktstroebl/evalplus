
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
    
    # set the variable to be last character of txt
    last_char = txt[-1]
    last_char_is_alpha = last_char.isalpha()
    last_char_is_non_word = (not last_char.isspace())
    
    # evaluate logic
    return last_char_is_alpha and last_char_is_non_word
