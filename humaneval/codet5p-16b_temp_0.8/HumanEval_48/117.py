

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
    left = 0
    right = len(text)-1
    
    while left <= right:
        if text[left] == text[right]:
            left += 1
            right -= 1
        else:
            return False
        
    return True
    
    
