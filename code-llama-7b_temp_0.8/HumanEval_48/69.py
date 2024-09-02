

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
    # The reversed version of the input text is created using a slice of the input string starting at index -1 and
    # stepping backwards by -1 each time. For example, the string 'zbcdef' would become 'fedcba'.
    return text == text[::-1]
