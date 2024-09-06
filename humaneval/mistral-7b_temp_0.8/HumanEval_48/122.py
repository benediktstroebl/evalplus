

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
    # You are welcome to use the following helper methods.
    def is_string_palindrome(text: str) -> bool:
        """
        Checks if given string is a palindrome
        >>> is_string_palindrome('')
        True
        >>> is_string_palindrome('aba')
        True
        >>> is_string_palindrome('aaaaa')
        True
        >>> is_string_palindrome('zbcd')
        False
        """
        return text == text[::-1]

    def is_list_palindrome(text: str) -> bool:
        """
        Checks if given string is a palindrome
        >>> is_list_palindrome('')
        True
        >>> is_list_palindrome('aba')
        True
        >>> is_list_palindrome('aaaaa')
        True
        >>> is_list_palindrome('zbcd')
        False
        """
        return text == list(text)[::-1]

    if is_string_palindrome(text):
        return
