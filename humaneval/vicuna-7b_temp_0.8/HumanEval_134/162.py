
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
    word_found = False
    for c in txt[::-1]:
        if word_found:
            if not re.match(r'\w', c):
                word_found = False
        elif c.isalpha() and c != last_char and not re.match(r'\w', c):
            word_found = True
        last_char = c
    return word_found