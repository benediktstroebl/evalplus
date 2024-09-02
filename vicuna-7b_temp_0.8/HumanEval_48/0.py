

def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    # if string is empty return True
    if len(text) == 0:
        return True
    # split string into list of characters
    words = text.split()
    # sort words
    words.sort()
    # concatenate words in reverse order to get original string
    return words[::-1] == text