def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    # Convert string to list to allow reversed iterating
    # Start loop from the middle of the list, and compare iterations
    return text == text[::-1][:len(text) // 2][::-1]