

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
    if not text:
        return True

    if not isinstance(text, str):
        raise TypeError

    if not text.strip():
        return True

    # if there is one character, it is a palindrome
    if len(text) == 1:
        return True

    # if there are two characters, they are palindromes if they're the same
    if len(text) == 2:
        return text[0] == text[-1]

    # if the first and final characters aren't the same, we don't count it
    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])

