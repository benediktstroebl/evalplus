

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
    if len(text) == 1:
        return True
    if len(text) % 2 == 1:
        if text[0] != text[-1]:
            return False
        else:
            return is_palindrome(text[1:-1])
    if len(text) % 2 == 0:
        if text[0] != text[-1]:
            return False
        else:
            return is_palindrome(text[1:-1])
    

