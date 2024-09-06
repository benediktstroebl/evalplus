
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
    # My code
    def last_char(txt):
        txt = txt.split()
        return txt[-1][-1]
    
    lst = last_char(txt)
    if lst.isalpha() and lst not in 'aeiou':
        return True
    else:
        return False


    # Given solution
    txt = txt.split()
    return txt[-1][-1].isalpha() and txt[-1][-1] not in 'aeiou'

