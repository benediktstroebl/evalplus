
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

    # type your code here

    txt_len = len(txt)
    txt_char = txt[txt_len - 1]

    if (txt_len == 0):
        return False

    if (txt_len == 1):
        return txt_char.isalpha()

    if (txt_len > 1):
        if (txt[txt_len - 2] == " "):
            return txt_char.isalpha()
        else:
            return False
