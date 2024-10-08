

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
    # for an empty string, the result is True
    if not text:
        return True

    left_idx = 0
    right_idx = len(text) - 1

    # only check for the first half of the string
    while left_idx < right_idx:
        if text[left_idx] != text[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1

    return True

