

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
    length = len(text)
    middle = length // 2

    if length % 2 == 0:
        return text[:middle] == text[middle:][::-1]
    else:
        return text[:middle] == text[middle + 1:][::-1]

