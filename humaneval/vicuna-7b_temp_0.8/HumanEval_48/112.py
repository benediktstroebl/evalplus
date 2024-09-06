

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
    # if string is empty, it is a palindrome
    if len(text) == 0:
        return True
    # split the string into two parts
    left_part, right_part = text[:len(text)//2], text[len(text)//2:]
    # check if the two parts are equal
    return left_part == right_part