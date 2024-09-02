
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
    # If length of string is 0, return false
    if len(txt) == 0:
        return False
    # Else if last character is not a letter, return false
    elif not txt[-1].isalpha():
        return False
    # Else if last character is a letter, check if it is not a part of a word
    elif txt[-1].isalpha():
        return check_if_last_char_is_a_letter_in_a_word(txt)

