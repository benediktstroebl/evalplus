
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
    last_char = txt[-1]
    if len(txt) == 0 or txt[len(txt)-1] == ' ' or txt[len(txt)-1] == '\n' or txt[len(txt)-1] == '\t':
        return False
    word = txt[:-1].split()
    if word:
        if any(c.isalpha() for c in word[-1]):
            if not any(c.isalpha() for c in word[-1]):
                return True
    else:
        return True
