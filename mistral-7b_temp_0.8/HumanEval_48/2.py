

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

    # If it is an empty string, return True
    if len(text) == 0:
        return True

    # If the first and last character are not the same, return False
    if text[0] != text[-1]:
        return False

    # Remove the first and last characters from the string
    new_text = text[1:-1]

    # Recursively call the function on the new string
    return is_palindrome(new_text)

