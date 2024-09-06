

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

    reverse = ""

    for i in range(len(text) - 1, -1, -1):
        reverse += text[i]
    if reverse == text:
        return True
    else:
        return False
