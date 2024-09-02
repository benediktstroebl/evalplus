

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
    # palindrome_checker
    length = len(text)
    if length < 2:
        return True
    for i in range(length // 2):
        if text[i] != text[length - i - 1]:
            return False
    return True

