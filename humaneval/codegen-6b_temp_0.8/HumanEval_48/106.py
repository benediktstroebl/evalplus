

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
    track = 0
    for ch in text:
        if ch == text[len(text) - 1 - track]:
            track += 1
    return track == len(text)

