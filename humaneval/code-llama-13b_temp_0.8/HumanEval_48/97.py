

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

    # start from first and last chars
    left = 0
    right = len(text) - 1

    # if not palindrome, then break
    while left < right:
        # if chars are not the same, break
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    # if we get here, the string is a palindrome
    return True

