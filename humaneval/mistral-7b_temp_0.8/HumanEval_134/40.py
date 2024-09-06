
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

    # Your code here
    txt_str = txt.split()
    last_word = txt_str[-1]
    last_word_str = last_word.strip()
    last_char = last_word_str[-1]

    if last_char.isalpha() and last_word_str[-1] != " ":
        return True
    else:
        return False

    '''
    To get the last word, you can split the string on spaces and take the last element of the resulting list.
    To get the last character of a string, you can use the -1 index of the string.
    To check if a character is alphabetical, you can use the isalpha() method of the str class.
    If the last character is alphabetical and not a space, the function should return True.
    Otherwise, it should return False.
    '''
