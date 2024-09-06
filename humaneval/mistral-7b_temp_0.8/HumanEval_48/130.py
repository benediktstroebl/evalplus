

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
    # if text == text[::-1]:
    #     return True
    # else:
    #     return False

    # reverse_text = text[::-1]
    # if reverse_text == text:
    #     return True
    # else:
    #     return False

    return text == text[::-1]

