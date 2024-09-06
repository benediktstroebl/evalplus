
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
    # [::-1] reverses string
    if txt[-1].isalpha():
        # split string into list by whitespace
        txt_list = txt.split()
        # add back together in reverse order with no space
        txt = "".join(txt_list[::-1])
        # return true if last character is not a space
        return txt[-1] != " "
    return False
