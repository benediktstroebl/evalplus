
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

    # convert txt to string
    txt = str(txt)
    # split the string into a list of words
    txt_list = txt.split()
    # if txt is not empty
    if txt_list:
        # get the last letter of the last word in txt
        txt_last_letter = txt_list[-1][-1]
        # check if txt_last_letter is a letter
        if txt_last_letter.isalpha():
            # check if txt_last_letter is not a part of a word
            if txt_last_letter not in txt_list[-1][:-1]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

