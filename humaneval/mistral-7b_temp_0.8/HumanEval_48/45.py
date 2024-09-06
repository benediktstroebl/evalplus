

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
    # YOUR CODE HERE
    text = text.lower()
    text = text.strip(' ')
    text = text.replace(' ', '')
    return text == text[::-1]
