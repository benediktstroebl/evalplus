
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
    check_if_last_char_is_a_letter = ''
    check_if_last_char_is_a_letter = txt[len(txt)-1]
    txt = txt.split()
    if check_if_last_char_is_a_letter.isalpha():
        check_if_last_char_is_a_letter = True
        return check_if_last_char_is_a_letter
    else:
        check_if_last_char_is_a_letter = False
        return check_if_last_char_is_a_letter


