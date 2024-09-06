

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
    # Check if string is empty
    if len(text) == 0:
        return True
    
    # Convert string to lowercase
    text = text.lower()
    
    # Check if string is a palindrome
    if text == text[::-1]:
        return True
    
    return False
