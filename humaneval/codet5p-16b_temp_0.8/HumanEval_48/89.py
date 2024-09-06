

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
    text = text.lower()
    reverse = []
    for index in range(len(text) - 1, -1, -1):
        reverse.append(text[index])
    return text == ''.join(reverse)

