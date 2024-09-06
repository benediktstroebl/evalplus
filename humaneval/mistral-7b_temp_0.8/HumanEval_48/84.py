

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

    def palindrome(text: str) -> bool:
        if len(text) <= 1:
            return True
        return text[0] == text[-1] and palindrome(text[1:-1])

    return palindrome(text)

