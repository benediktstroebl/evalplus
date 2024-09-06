

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
    if len(text) < 2:
        return True
    else:
        first_half = text[:len(text) // 2]
        second_half = text[len(text) // 2:]
        return is_palindrome(first_half) and is_palindrome(second_half)

