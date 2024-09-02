

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
    left_pos = 0
    right_pos = len(text) - 1

    while left_pos < right_pos:
        if text[left_pos] != text[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
    return True

