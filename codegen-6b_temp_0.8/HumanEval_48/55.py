

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
    # We'll treat the entire string as upper-cased here
    text = text.upper()
    # Return if we've made no progress on reversing the string
    if text == text[::-1]:
        return True
    else:
        return False

