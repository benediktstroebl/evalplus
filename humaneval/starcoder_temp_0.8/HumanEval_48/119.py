

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
    i = 0
    j = len(text) - 1

    while i < j:
        if text[i]!= text[j]:
            return False
        i += 1
        j -= 1

    return True
