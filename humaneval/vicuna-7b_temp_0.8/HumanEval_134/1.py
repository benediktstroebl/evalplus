
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
    last_word = words[-1]
    last_char = last_word.lower()[-1]
    if last_char in string.punctuation and len(last_word) == 1:
        return True
    if last_char in string.ascii_letters and last_word.count(" ") == 0:
        return True
    else:
        return False