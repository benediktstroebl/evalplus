

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
    if len(text) % 2 == 1:
        return is_palindrome(text[:int((len(text) - 1) / 2)]) and is_palindrome(text[int((len(text) + 1) / 2):])
    return is_palindrome(text[:int(len(text) / 2)]) and is_palindrome(text[int(len(text) / 2):][::-1])

