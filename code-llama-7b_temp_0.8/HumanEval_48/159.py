

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
    # make text lowercase, remove space, punctuation
    text = text.lower()
    text = ''.join(text.split())
    # iterate through text and reverse it
    reversed_text = text[::-1]
    # check if they match
    return text == reversed_text

