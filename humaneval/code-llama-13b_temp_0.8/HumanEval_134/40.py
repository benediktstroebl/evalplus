
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
    letters = 'abcdefghijklmnopqrstuvwxyz'
    if len(txt) == 0:
        return False
    if txt[-1] in letters:
        return False
    else:
        return True
    
    
    
    #return txt[-1] in letters and txt.split(' ')[-1] != txt[-1]
    
    '''
    txt = 'apple pie'
    txt[-1]
    txt.split(' ')
    txt[-1] in txt.split(' ')
    '''
