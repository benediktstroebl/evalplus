

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

    i = 0
    j = len(text) - 1
    while i <= j:
        while not text[i].isalnum() and i < j:
            i += 1
        while not text[j].isalnum() and i < j:
            j -= 1
        if text[i].lower()!= text[j].lower():
            return False
        i += 1
        j -= 1
    return True
