
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

    # Check if the last character is a letter and not a part of a word.
    if txt.endswith(" ") or txt.endswith(".") or txt.endswith("?") or txt.endswith("!") or txt.endswith(":") or txt.endswith(";"):
        return False
    # If the last character is a letter and not a part of a word, return True.
    if txt.endswith("a") or txt.endswith("b") or txt.endswith("c") or txt.endswith("d") or txt.endswith("e") or txt.endswith("f") or txt.endswith("g") or txt.endswith("h") or txt.endswith("i") or txt.endswith("j") or txt.endswith("k") or txt.endswith("l") or txt.endswith("m") or txt.endswith("n") or txt.endswith("o") or txt.endswith("p") or txt.endswith("q") or txt.
