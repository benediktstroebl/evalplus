

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
    if text == '':
        return True
    if len(text) == 1:
        return True
    if text[0] == text[-1]:
        return is_palindrome(text[1:len(text)-1])
    else:
        return False

