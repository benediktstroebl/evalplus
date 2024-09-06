

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
    input_length = len(text)
    if input_length == 0:
        return True
    mid_index = input_length // 2
    if text[0:mid_index] == text[-1:-mid_index - 1:-1]:
        return True
    return False
