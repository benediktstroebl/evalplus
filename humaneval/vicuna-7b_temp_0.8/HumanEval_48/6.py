

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
    
    # check for single character
    if len(text) == 1:
        return text == text[::-1]
    
    # check for palindrome
    for i in range(len(text) // 2):
        if text[i] != text[i + len(text) // 2]:
            return False
    return True
