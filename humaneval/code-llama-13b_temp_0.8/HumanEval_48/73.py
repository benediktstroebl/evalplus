

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

    # O(n) time
    # O(n) space
    text = text.lower()
    text = text.replace(' ', '')
    return text == text[::-1]

