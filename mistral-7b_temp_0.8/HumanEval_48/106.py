

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
    # Do not change code above this line
    if text.isalnum() == False:
        return False
    text = text.lower()
    if text == text[::-1]:
        return True
    else:
        return False
    # Do not change code below this line

