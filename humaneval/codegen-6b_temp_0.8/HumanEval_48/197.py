

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
    # We use two pointers, one at start and one at the end
    # Start by setting both pointers to the start
    # While middle is less than the end
    # Check if the characters match
    # If so, increment start
    # Else, set middle to middle-1
    # Set start to middle+1
    # If middle is higher than the start, set middle to the start
    # Else, set start to the end

    start = 0
    end = len(text) - 1
    while start <= end:
        if text[start] != text[end]:
            return False
        start += 1
        end -= 1
    return True
