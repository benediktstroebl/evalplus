

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
    # check for empty string
    if not text:
        return True
    
    # check if text is a palindrome
    for i in range(len(text)):
        if text[i] != text[len(text)-i-1]:
            return False
    return True