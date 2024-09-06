
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
    
    # code goes here
    # try with a loop for each character in the string
    # use the startswith() function to see if the last character is a space
    # if it is a space, then check if the character before is an alphabetical character
    # if it is not, then return true
    # else, return false
    last_char = txt[-1]
    for char in txt:
        if char.isspace():
            if last_char.isalpha():
                return True
            return False
        
