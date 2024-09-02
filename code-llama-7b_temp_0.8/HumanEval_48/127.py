

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

    text = text.replace(' ', '')
    text = text.lower()
    i = 0
    j = len(text) - 1
    is_palindrome = True
    while i < j and is_palindrome:
        if text[i] != text[j]:
            is_palindrome = False
        i += 1
        j -= 1

    return is_palindrome

