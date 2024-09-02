
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
    if txt == "":
        return False
    txt_len = len(txt)
    if txt_len == 1:
        return False
    if txt_len == 2:
        if txt[0].isalpha() and txt[1] == " ":
            return True
    if txt_len >= 3:
        if txt[-1] == " ":
            return False
        if txt[-1].isalpha():
            return True
    return False
    
assert check_if_last_char_is_a_letter("") == False
assert check_if_last_char_is_a_letter("applepie") == False
assert check_if_last_char_is_a_letter("applpie") == True
assert check_if_last_char_is_a_letter("applepi e") == True
assert check_if_last_char_is_a_letter("applepi e ") == False
assert check_if_last_char_is_a_letter("applepi e") == False
assert check_if_last_char_is_a_letter("apple pi e") == False
assert check_if_last_char_is_a_letter("apple pi e ") == True
assert check_if_last_char_is_a_letter("applepi e") == True
assert check_if_last_char_is_a_letter("apple pi e ") == True


