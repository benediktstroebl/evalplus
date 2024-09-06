

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
    # reverse the text
    reverse_text = text[::-1]
    # compare the reverse text and the original text
    if reverse_text == text:
        return True
    else:
        return False

