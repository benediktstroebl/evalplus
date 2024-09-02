
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


    # try:
    #     for i in txt:
    #         if i == " " and txt.index(i) == len(txt) - 1:
    #             return False
    #         elif i.isalpha():
    #             return True
    #     return False

    # end try

    # try:
    #     if txt[-1].isalpha() and txt.index(txt[-1]) == len(txt) - 1:
    #         return True
    #     else:
    #         return False
    # except:
    #     pass

    # try:
    #     for i in txt:
    #         if i.isalpha() and i == txt[-1] and txt.index(txt[-1]) == len(txt) - 1:
    #             return True
    #     return False
    # except:
    #     pass

    # try:
    #     for i in txt:
    #         if i == " " and txt.index(i) == len(txt) - 1:
    #             return False
