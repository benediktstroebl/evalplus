
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
    return ''.join(re.findall(r'[a-z]+$', txt))
    # return not ''.join(re.findall(r'[a-zA-Z]+$', txt))
    # return ''.join(re.findall(r'[a-z]+$', txt)) and not ''.join(re.findall(r'[a-zA-Z]+$', txt))
    # return True if ''.join(re.findall(r'[a-z]+$', txt)) and not ''.join(re.findall(r'[a-zA-Z]+$', txt)) else False
    # return True if ''.join(re.findall(r'[a-z]+$', txt)) and not ''.join(re.findall(r'[a-zA-Z]+$', txt)) else False
    # return True if re.findall(r'[a-z]+$', txt) and not re.findall(r'[a-zA-Z]+$', txt) else False
    # return True if
