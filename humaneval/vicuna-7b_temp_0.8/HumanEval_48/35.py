

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
    # check if string is empty
    if len(text) == 0:
        return True

    # check if string is palindrome
    if not text:
        return True

    # split the string into two parts
    left = text[:len(text) // 2]
    right = text[len(text) // 2:]

    # check if both parts are equal
    if not left == right:
        return False

    # check if both parts are equal
    return True