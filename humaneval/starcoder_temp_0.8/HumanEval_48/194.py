

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
    
    text = text.lower()
    middle = len(text) // 2
    text = text[:middle] + text[middle+1:]
    return text == text[::-1]
