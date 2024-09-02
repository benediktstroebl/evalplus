

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
    if text == '':
        return True

    for i in range(0, len(text) // 2 + 1):
        if text[i]!= text[-(i+1)]:
            return False
    return True

