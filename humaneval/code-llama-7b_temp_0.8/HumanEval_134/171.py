
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
    
    if (txt == ''):
        return False
    
    # split the string into words
    txt_list = txt.split(' ')
    
    # get the last word from the list
    last_word = txt_list[-1]
    
    # get the last character from the last word
    last_letter = last_word[-1]
    
    # check if the last letter is an alphabetical letter
    if last_letter.isalpha():
        return False
    
    return True

