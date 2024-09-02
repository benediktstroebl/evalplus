

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
    i, j = 0, len(text) - 1
    while i < j:
        if not text[i].isalnum():
            i += 1
            continue
        if not text[j].isalnum():
            j -= 1
            continue
        if text[i] == text[j]:
            i += 1
            j -= 1
            continue
        return False
    return True

