

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
    # We use negative index of the string for even-indexed characters
    # and positive index for odd-indexed characters
    # O(n)
    for i in range(len(text) // 2):
        if text[i] != text[-i-1]:
            return False
    return True
