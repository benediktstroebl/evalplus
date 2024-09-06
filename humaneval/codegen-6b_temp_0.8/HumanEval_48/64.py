

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
    index = 0
    result = True
    while index < len(text) // 2:
        if text[index] != text[len(text) - index - 1]:
            result = False
            break
        index += 1
    return result

