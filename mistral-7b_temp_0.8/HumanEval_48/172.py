

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
    if not text:
        return True
    text = text.lower()
    middle = len(text) // 2
    if len(text) % 2 == 0:
        left, right = 0, middle
    else:
        left, right = 0, middle - 1

    for i in range(left, right):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True

