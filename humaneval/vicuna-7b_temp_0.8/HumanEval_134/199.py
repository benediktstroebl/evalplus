
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
    words = txt.split()
    last_word = ""
    last_char = txt[-1]
    last_char_is_letter = False
    last_char_is_word = False
    for word in words:
        if word[-1] == last_char:
            last_char_is_letter = True
            last_char_is_word = True
            break
        last_word += word
    if last_char_is_letter and last_char_is_word == False:
        return True
    else:
        return False
