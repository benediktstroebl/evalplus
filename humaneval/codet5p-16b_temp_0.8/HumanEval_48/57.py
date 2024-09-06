

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

    is_palindrome = True
    if len(text) < 2:
        return is_palindrome
    for i in range(len(text)//2):
        if text[i]!= text[-(i+1)]:
            is_palindrome = False
    return is_palindrome
