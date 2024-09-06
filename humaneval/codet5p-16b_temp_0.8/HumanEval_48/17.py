

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

    left_index, right_index = 0, len(text) - 1
    while left_index < right_index:
        if not text[left_index].isalnum():
            left_index += 1
            continue
        if not text[right_index].isalnum():
            right_index -= 1
            continue
        if text[left_index].lower()!= text[right_index].lower():
            return False
        left_index += 1
        right_index -= 1
    return True

