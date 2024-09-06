

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

    left_index = 0
    right_index = len(text) - 1
    while left_index < right_index:
        if text[left_index] != text[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True
