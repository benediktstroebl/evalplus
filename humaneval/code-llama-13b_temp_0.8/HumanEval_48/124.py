

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
    text_length = len(text)
    if text_length <= 1:
        return True
    # check if both sides are the same
    left_index = 0
    right_index = text_length - 1

    while left_index < right_index:
        left_char = text[left_index]
        right_char = text[right_index]
        if left_char != right_char:
            return False
        left_index += 1
        right_index -= 1
    return True

