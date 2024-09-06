

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
    def is_palindrome_helper(text):
        if not text:
            return True

        if text[0] != text[-1]:
            return False

        return is_palindrome_helper(text[1:-1])
    return is_palindrome_helper(text)
