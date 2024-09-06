

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

    front = 0
    back = len(text) - 1
    while front < back:
        if text[front] != text[back]:
            return False
        front += 1
        back -= 1
    return True

