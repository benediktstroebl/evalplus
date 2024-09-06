

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
    text_left = 0
    text_right = len(text) - 1

    while text_left < text_right:
        if text[text_left] != text[text_right]:
            return False
        text_left += 1
        text_right -= 1
    return True
