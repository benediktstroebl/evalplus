
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
    if txt == "" or txt == " ":
        return False
    if len(txt) > 1:
        last_char = txt[-1]
        dist_from_start = len(txt) - 1
        dist_from_end = len(txt) - 1 - len(txt.rstrip(" "))
        if dist_from_start == dist_from_end: #if first and last are letters
            if dist_from_start != 0:
                if last_char.isalpha():
                    if not last_char.lower() in string.punctuation:
                        return True
        else:
            if last_char.isalpha():
                if not last_char.lower() in string.punctuation:
                    return True
    return False
