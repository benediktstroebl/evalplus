
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
    # 1. check if txt is empty.
    # 2. check if txt is an alphabet character.
    # 3. check if txt is a space.
    # 4. check if txt is a word (contains a space).
    # 5. check if txt[len(txt)-1] is a word (contains a space).
    # 6. check if txt[len(txt)-1] is not a space.

    if not txt:
        return False
    elif txt[-1].isalpha():
        return True
    elif ' ' not in txt:
        return False
    elif ' ' in txt:
        for word in txt.split(' '):
            if word[-1].isalpha() and word[0].isalpha():
                return True
            elif word[-1].isalpha() and word[0].isspace():
                return False
            elif word[-1].isspace() and word[0].isspace():
                return False
            elif word[-1].isspace() and word[0].isalpha():
                return True
            else:
                return False

