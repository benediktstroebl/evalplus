

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
    # check if string is empty, and if it is, return True
    if not text:
        return True

    # if not, check if string is a palindrome using reverse string
    # to compare
    reversed_text = text[::-1]
    return text == reversed_text

