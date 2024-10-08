

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
    text = text.lower()
    text = text.replace(' ', '')
    for i in range(len(text) // 2):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True

