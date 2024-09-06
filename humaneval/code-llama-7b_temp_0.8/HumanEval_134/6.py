
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
    # Create a list with words in txt using the split() method.
    txt_list = txt.split()
    
    # If txt is not empty then get the last word, if it ends with an alphabetical character return True, otherwise False.
    # If txt is empty return False.
    if txt:
        last_word = txt_list[-1]
        if last_word[-1].isalpha():
            return True
        else:
            return False
    else:
        return False
