
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

    txt = txt.strip()

    if len(txt) == 0:
        return False

    last_char = txt[-1]
    # print(last_char)

    if last_char.isalpha():
        # print("is alpha")
        for i in range(len(txt)-1):
            if txt[i].isalpha():
                # print("is word")
                return False
        # print("is letter")
        return True

    return False

