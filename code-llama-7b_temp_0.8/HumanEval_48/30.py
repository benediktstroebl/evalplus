

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
    # palindrome_dict = {a: b for a, b in zip(text[::-1], text)}
    # return all(palindrome_dict.values())
    return text == text[::-1]

