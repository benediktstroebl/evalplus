

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
    trans_table = text.maketrans('', '', string.punctuation)
    text = text.translate(trans_table)
    if text == text[::-1]:
        return True
    return False

