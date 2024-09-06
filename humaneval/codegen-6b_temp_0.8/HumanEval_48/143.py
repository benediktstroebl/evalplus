

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
    start = 0
    end = len(text) - 1

    while start < end:
        if text[start] != text[end]:
            return False
        start += 1
        end -= 1
    return True

