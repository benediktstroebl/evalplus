

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
    # Initialize empty string to store the checksum
    checksum = ''

    # Iterate over the characters in the text
    for char in text:
        # Add the character to the checksum
        checksum += char

    # Check if the checksum is equal to the original text
    return checksum == text
