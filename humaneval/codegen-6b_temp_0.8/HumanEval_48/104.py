

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
    # Case 1: empty string
    if text == '':
        return True
    # Case 2: single character
    elif len(text) == 1:
        return True
    # Case 3: odd length
    elif len(text) % 2 == 1:
        # Get middle character
        mid = len(text) // 2
        if text[mid] != text[mid - 1]:
            return False
        else:
            return is_palindrome(text[:mid] + text[mid + 1:])
    # Case 4: even length
    else:
        mid_1 = len(text) // 2
        mid_2 = len(text) // 2 - 1
        if text[mid_1] != text[mid_2]:
            return False
        else:
            return is_palindrome(text[:mid_1] + text[mid_2 + 1:])

