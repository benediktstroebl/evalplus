
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
    
    txt = txt.replace(' ', '')
    txt_len = len(txt)
    if txt_len == 0:
        return False
    elif txt_len == 1:
        if txt[0].isalpha() == False:
            return False
        else:
            return True
    else:
        last_ch = txt[txt_len-1]
        if last_ch.isalpha() == False:
            return False
        else:
            return True
