
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

    # Using split()
    # txt.split()[-1][-1] == 'a' # False
    # txt.split()[-1][-1].isalpha() # True
    # txt.split()[-1][-1].isalnum() # True
    # txt.split()[-1][-1].isdigit() # False
    # txt.split()[-1][-1].isupper() # False
    # txt.split()[-1][-1].islower() # True
    # txt.split()[-1][-1].isnumeric() # False

    # Using regex:
    # txt[-1] == 'a' # False
    # txt[-1].isalpha() # True
    # txt[-1].isalnum() # True
    # txt[-1].isdigit() # False
    # txt[-1].isupper() # False
    # txt[-1].islower() # True
    # txt[-1].isnumeric() # False

    txt_list = txt.split()
    last_char = txt_list[-1][-1]
