

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

    # Make text lower case
    text = text.lower()

    # Remove all spaces
    text = text.replace(' ', '')

    # Reverse text
    reversed_text = text[::-1]

    # Check if text and reversed_text are equal
    if text == reversed_text:
        return True
    else:
        return False
