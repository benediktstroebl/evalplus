
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
    n = len(txt)
    last_char = txt[-1]
    word_end = txt[-1] == ' ' or txt[-1] == '\n' or txt[-1] == '.'
    # txt[-1] == ' ' or txt[-1] == '\n' or txt[-1] == '.'
    txt = txt.lower()
    txt = txt.replace(".", "")
    txt = txt.replace(" ", "")
    txt = txt.replace("\n", "")
    if last_char == last_char.upper():
        last_char = last_char.lower()
    if word_end == False:
        if last_char.isalpha():
            return True
        else:
            return False
    else:
        if last_char.isalpha():
            return False
        else:
            return False

