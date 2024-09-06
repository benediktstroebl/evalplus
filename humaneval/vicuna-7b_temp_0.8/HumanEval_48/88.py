

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
    if len(text) == 0:
        return True
    
    # check if the first and last character of the string is same
    if text[0] != text[-1]:
        return False
    
    # check if the middle characters are same
    middle_len = len(text) // 2
    if not text[middle_len:middle_len+1] == text[:middle_len]:
        return False
    
    return True