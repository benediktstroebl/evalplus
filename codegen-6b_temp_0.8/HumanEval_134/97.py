
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
    new_txt = txt.strip()
    new_txt = re.sub(r'\s', '', new_txt)
    only_letters = re.compile(r'[a-zA-Z]+').findall(new_txt)
    orig_len = len(only_letters)
    only_letters_len = len(only_letters)
    return True if only_letters_len == orig_len - 1 and \
                    only_letters[-1] not in [' ', '', '.'] else False

