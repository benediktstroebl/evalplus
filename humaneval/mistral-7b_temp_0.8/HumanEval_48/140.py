

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

    def helper(left: int, right: int):
        if left >= right:
            return True
        if text[left] != text[right]:
            return False
        return helper(left+1, right-1)

    return helper(0, len(text)-1)

