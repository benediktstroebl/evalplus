
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
    return True if txt[-1].isalpha() and not txt[-1].isnumeric() and txt[-1] != ' ' else False

    # NOTE: 
    # return True if txt[-1].isalpha() and not txt[-1].isnumeric() and txt[-1] != ' ' else False

    # NOTE:
    # if not txt[-1].isalpha():
    #     if not txt[-1].isnumeric():
    #         if txt[-1] != ' ':
    #             return True
    #     else:
    #         return True
    # else:
    #     return False

    # NOTE:
    # result = False
    # if txt[-1].isalpha():
    #     if txt[-1] != ' ':
    #         result = True
    # else:
    #     result = False
    # return result

    # def is_letter(s):
    #     return s.isalpha()

    # def is_number(s):
    #     return s.isnumeric()

    # if s[-1].isalpha():
    #     if s[-1] != ' ':
    #         return True
    # else:
    #     return False
