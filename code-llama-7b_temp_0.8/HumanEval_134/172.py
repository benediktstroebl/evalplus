
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

    # # Method 1
    # # Reference: https://stackoverflow.com/questions/268272/getting-the-last-element-of-a-list
    # if txt:
    #     if txt[-1].isalpha():
    #         return False
    #     else:
    #         return True
    # else:
    #     return False

    # # Method 2
    # if txt:
    #     word = txt.split()[-1]
    #     if word[-1].isalpha():
    #         return False
    #     else:
    #         return True
    # else:
    #     return False

    # Method 3
    if txt:
        if txt[-1].isalpha() and txt[-1] == ' ':
            return True
        else:
            return False
    else:
        return False
    
