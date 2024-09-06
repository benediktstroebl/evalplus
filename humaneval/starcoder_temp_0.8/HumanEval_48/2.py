

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
    
    text = ''.join(x for x in text.lower() if x in ascii_lowercase)
    for i, j in zip(text, reversed(text)):
        if i!= j:
            return False
    return True
