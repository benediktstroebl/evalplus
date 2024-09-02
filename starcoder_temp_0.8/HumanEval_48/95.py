

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
    
    # Get text length
    text_len = len(text)
    
    # Iterate over the text
    for i in range(text_len // 2):
        if text[i]!= text[text_len - i - 1]:
            return False
    
    return True
