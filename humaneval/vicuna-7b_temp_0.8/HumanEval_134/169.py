
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
    # check if the string is empty or not
    if txt == "":
        return False
    
    # split the string by space and get the last word
    last_word = txt.split()[-1]
    
    # check if the last word is empty or not
    if len(last_word) == 0:
        return True
    
    # check if the last character is alphabetical and not part of a word
    if last_word[0].isalpha() and last_word[-1] != last_word[0]:
        return True
    
    else:
        return False
