

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
    length = len(text)
    if length == 1:
        return True
    middle = length//2
    if text[0] != text[length-1]:
        return False
    return is_palindrome(text[1:middle+1])

