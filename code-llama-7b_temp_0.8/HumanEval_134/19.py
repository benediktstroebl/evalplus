
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
    # Create a variable that will store the last character of a given string.
    last_char = txt[-1]
    
    # Create a variable that will store the last character of a given string, as a number.
    last_num = ord(last_char)

    # Create a variable that will store the last character of a given string, as a boolean.
    last_bool = last_num > 64 and last_num < 91 or last_num > 96 and last_num < 123
    
    # If the last character is a letter, AND the last character is NOT a part of a word, then return True.
    if (last_bool and txt[-2] == " "):
        return True

    # If the last character is a letter, BUT the last character is a part of a word, then return False.
    elif (last_bool and txt[-2] != " "):
        return False
    
    # If the last character is NOT a letter, then return False.
    elif not last_bool:
        return False

