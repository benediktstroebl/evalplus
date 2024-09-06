

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

    left = 0
    right = len(text) - 1

    while right > left:
        if not text[left].isalpha():
            left += 1
        if not text[right].isalpha():
            right -= 1
        elif text[left].lower()!= text[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True

