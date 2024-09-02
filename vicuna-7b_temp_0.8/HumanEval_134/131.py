
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
    # Check if the string is not empty
    if txt:
        # Get the length of the string
        length = len(txt)
        # Get the last character
        last_char = txt[-1]
        # Check if the last character is a letter
        if not last_char.isalpha():
            return False
        # Check if the last character is not a part of a word
        for i in range(length-1, -1, -1):
            # Check if the current character is a space
            if txt[i].isspace():
                continue
            # Check if the current character is a letter
            if not txt[i].isalpha():
                return False
            # Check if the current character is not a part of a word
            if not txt[i].isalnum():
                return False
        # Return True if the last character is a letter and is not a part of a word, False otherwise
        return True
    return False