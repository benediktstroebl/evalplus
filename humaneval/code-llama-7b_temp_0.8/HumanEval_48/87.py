

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
    if len(text) == 0 or len(text) == 1:
        return True
    elif len(text) == 2:
        if text[0] == text[1]:
            return True
        else:
            return False
    else:
        if text[0] == text[len(text)-1]:
            return is_palindrome(text[1:len(text)-1])
        else:
            return False

