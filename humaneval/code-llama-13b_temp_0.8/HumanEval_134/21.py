
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

    return txt[-1].isalpha() and txt.rstrip()[-1] == txt.split(' ')[-1][-1]

    '''
    Alternative solutions
    # Method 1
    return txt and txt.rstrip()[-1] == txt.split()[-1][-1] and txt.rstrip()[-1].isalpha()
    
    # Method 2
    s = txt.rstrip()
    last_char = s[-1]
    return s and last_char.isalpha() and last_char == s.split()[-1][-1]
    '''
