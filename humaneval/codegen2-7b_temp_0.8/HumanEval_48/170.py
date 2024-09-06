

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

    first_half = text[:len(text)//2]
    second_half = text[len(text)//2:]

    return first_half == second_half[::-1
