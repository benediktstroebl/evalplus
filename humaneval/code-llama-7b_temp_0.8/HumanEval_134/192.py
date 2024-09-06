
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
    # new_text = txt.split(" ")
    # for i in new_text:
    #     if i == "":
    #         return False
    #     if not i[-1].isalpha():
    #         return False
    #     if i[-1].isalpha():
    #         return True
    
    return True if txt[-1].isalpha() and " " in txt else False
