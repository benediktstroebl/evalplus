
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
    return False

assert check_if_last_char_is_a_letter("apple pie") == False,\
    'Expected False, got {}'.format(check_if_last_char_is_a_letter("apple pie"))
assert check_if_last_char_is_a_letter("apple pi e") == True,\
    'Expected True, got {}'.format(check_if_last_char_is_a_letter("apple pi e"))
assert check_if_last_char_is_a_letter("apple pi e ") == False,\
    'Expected False, got {}'.format(check_if_last_char_is_a_letter("apple pi e "))
assert check_if_last_char_is_a_letter("") == False,\
    'Expected False, got {}'.format(check_if_last_char_is_a_letter(""))
assert check_if_last_char_is_a_letter("foo") == False,\
    'Expected False, got {}'.format(check_if_last_char_is_a_letter("foo"))
assert check_if_last_char_is_a_letter("foo bar") == False,\
    'Expected False, got {}'.format(check_if_last_char_is_a_letter("foo bar"))
assert check_if_last_char_is_a_letter("foo barbaz") == False,\
    'Expected False, got {}'.format(check_if_last_char_is_a_letter("foo barbaz"))
assert check_if_last_char_is_a_letter("foo barba") == True,\
    'Expected True, got {}'.format(check_if_last_char_is_a_letter("foo barba"))
assert check_if_last_char_is_a_letter("foo barba baz") == False,\
    'Expected False, got {}'.format(check_if_last_char_is_a_letter("foo barba baz"))
assert check_if_last_char_is_a_letter("foo barba\nbaz") == False,\
