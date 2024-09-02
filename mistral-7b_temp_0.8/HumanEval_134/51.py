
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
    txt_lst = list(txt)
    if not txt:
        return False

    txt_lst = txt_lst[:-1]
    if not any(char.isalpha() for char in txt_lst):
        return False

    if txt_lst[-1].isalpha():
        return False
    else:
        return True

    txt_lst = txt_lst[:-1]
    if not any(char.isalpha() for char in txt_lst):
        return False

    if txt_lst[-1].isalpha():
        return False
    else:
        return True

    txt_lst = txt_lst[:-1]
    if not any(char.isalpha() for char in txt_lst):
        return False

    if txt_lst[-1].isalpha():
        return False
    else:
        return True

    txt_lst = txt_lst[:-1]
    if not any(char.isalpha() for char in txt_lst):
        return False

    if txt_lst[-1].isalpha():
        return False
