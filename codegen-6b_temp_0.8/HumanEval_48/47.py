

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
    # We treat the string as a queue and only add and remove right-most characters
    # from the front and back of the string.
    # Because the string is probably shorter than 100 characters, we can use
    # this optimization in O(n) time.
    left = 0
    right = len(text) - 1
    while left < right:
        while not text[left].isalnum() and left < right:
            left += 1
        while not text[right].isalnum() and left < right:
            right -= 1
        if text[left].lower() != text[right].lower():
            return False
        left += 1
        right -= 1
    return True

