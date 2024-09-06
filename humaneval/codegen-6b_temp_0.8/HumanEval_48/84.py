

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
    start_index = 0
    end_index = len(text) - 1

    while end_index > start_index:
        if text[start_index] != text[end_index]:
            return False
        start_index += 1
        end_index -= 1

    return True

