
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
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    words = txt.split()
    for i in letters:
        if txt.count(i) >= 1:
            if txt[-1] == i:
                if len(words) == 0:
                    return False
                else:
                    if len(words) >= 1:
                        if words[-1] == i:
                            return False
                    else:
                        return True
            else:
                return True
        else:
            return False
        
    return False

    
