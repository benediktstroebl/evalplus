

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
    # Use a for loop to iterate through the string, pairing each character with its reverse
    for i in range(len(text) // 2):
        if text[i] != text[len(text) - i - 1]:
            return False
    return True