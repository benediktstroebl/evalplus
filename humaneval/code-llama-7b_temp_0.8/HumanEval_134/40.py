
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
    # 1. Split the string to check into a list of words.
    txt = txt.split()
    
    # 2. Iterate over the list, and check if the last letter in each word is an alphabetical letter.
    for i in txt:
        if i[-1].isalpha() == True:
            return True
        else:
            continue
    return False

