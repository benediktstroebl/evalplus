

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
    # make a copy of the string
    new_text = text[:]
    # to compare the original to the reversed string, we will reverse the string
    for i in range(len(text)):
        new_text[i] = new_text[len(text) - 1 - i]
    return new_text == text

