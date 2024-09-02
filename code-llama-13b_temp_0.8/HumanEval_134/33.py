
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
    if txt == '':
        return False

    # split words
    words = txt.split(' ')
    last_word = words[-1]

    # check for last letter
    last_char = last_word[-1]
    last_char_idx = len(last_word) - 1
    is_last_letter_in_word = last_char_idx == len(last_word) - 1
    is_last_char_letter = last_char.isalpha()

    return is_last_letter_in_word and is_last_char_letter

