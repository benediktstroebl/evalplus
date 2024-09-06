
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
    # Check if the last char is a word
    last_word = re.split("[ ]", txt)[-1]
    if last_word:
        # Check if the last char is a letter and is not a part of the word
        last_char = last_word[-1]
        if last_char.isalpha() and last_char != last_word[-1]:
            return True
    return False