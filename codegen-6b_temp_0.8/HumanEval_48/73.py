

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
    # Runtime: O(n)
    # Spacetime: O(1)
    l = 0
    r = len(text) - 1
    while l < r:
        if text[l] != text[r]:
            return False
        l += 1
        r -= 1
    return True

