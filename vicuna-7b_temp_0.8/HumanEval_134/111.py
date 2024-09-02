
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
    # Check if txt is empty
    if txt == "":
        return False
    # Check if the last character is a digit
    if txt[-1].isdigit():
        return True
    # Check if the last character is a letter
    if not any(txt[-1] in letter for letter in string.ascii_letters):
        return True
    # Check if the last character is part of a word
    word = " ".join(txt[:-1])
    return not any(word)
