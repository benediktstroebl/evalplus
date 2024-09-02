

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

    # Strip all non-alphanumeric characters
    text = re.sub(r'\W', '', text, flags=re.I)

    # Lowercase all alphanumeric characters
    text = text.lower()

    # Compare first half of string to the last half
    return text == text[::-1]
