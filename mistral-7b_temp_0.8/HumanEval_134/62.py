
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
    if txt.strip():
        txt = txt.strip()
        last_char = txt[-1]
        txt = txt.replace(last_char, '')
        words = txt.split()
        if not words:
            return False
        if len(words) == 1:
            return True
        for i in range(len(words)):
            if last_char in words[i]:
                return False
        return True
    return False


