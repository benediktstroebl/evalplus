

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
    # idea:
    # use two pointers, fast and slow
    # if they point to the same char, and next char is not equal to the last char, return False
    # else move pointers
    # return True if fast pointer is at the end, else False
    # Time: O(n)
    # Space: O(1)
    if text == '':
        return True
    fast = slow = 0
    while fast < len(text) and text[slow] == text[fast]:
        fast += 1
        slow += 1
    return fast == len(text)
