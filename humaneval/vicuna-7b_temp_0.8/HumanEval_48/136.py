

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
    if len(text) == 0:
        return True
    elif len(text) == 1:
        return text == text[::-1]
    else:
        for i in range(len(text)-1, 0, -1):
            if text[i] != text[i][::-1]:
                return False
        return True