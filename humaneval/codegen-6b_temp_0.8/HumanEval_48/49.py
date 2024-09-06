

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
    else:
        first = 0
        last = len(text) - 1
        while first < last:
            if not text[first] == text[last]:
                return False
            first += 1
            last -= 1
        return True

