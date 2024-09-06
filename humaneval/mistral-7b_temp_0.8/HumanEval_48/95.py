

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

    if text.isdigit():
        return False
    if text.isalpha():
        text = text.lower()
        if len(text) < 2:
            return True
        else:
            return text[0] == text[-1] and is_palindrome(text[1:-1])
    return False


