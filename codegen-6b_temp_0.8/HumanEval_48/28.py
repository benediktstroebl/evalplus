

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

    if len(text) == 1:
        return True

    left_idx, right_idx = 0, len(text) - 1

    while left_idx < right_idx:
        if text[left_idx] != text[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1

    return True

