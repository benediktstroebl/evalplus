

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
    # step1: take two pointers at start and end of the string
    # step2: compare the chars
    # step3: if they are equal, increment both pointers
    # step4: if they are not, decrement the right pointer
    # step5: if the two pointers ever meet, it is a palindrome

    # step1:
    i, j = 0, len(text) - 1
    while i <= j:
        # step2:
        if text[i] != text[j]:
            return False
        # step3:
        i += 1
        j -= 1
    return True

