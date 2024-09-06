
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
    # Output:
    # True
    # False
    # False
    # False

    # Answer:
    def check_if_last_char_is_a_letter(txt):
        return txt.endswith(' ') or txt[-1] in '!.?'

    # An even shorter answer:
    def check_if_last_char_is_a_letter(txt):
        return txt.endswith(' ') or txt.endswith('!?')

    # Pythonic answer:
    def check_if_last_char_is_a_letter(txt):
        return txt.endswith(' ') or txt.endswith('!?')

    # Using Regex:
    def check_if_last_char_is_a_letter(txt):
        return re.search(r'\b\s\w\b', txt)
