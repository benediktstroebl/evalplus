

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
    if len(text) == 0:
        return True

    # split text into list of characters
    words = text.split()

    # reverse the words
    words = [word[::-1] for word in words]

    # join the words back into a string
    text = ''.join(words)

    # check if the string is equal to its reverse
    if text == reverse(text):
        return True
    else:
        return False
