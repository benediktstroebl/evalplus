

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
    text = text.lower()
    for i, letter in enumerate(text):
        if text[-i-1]!= letter:
            return False
    return True

