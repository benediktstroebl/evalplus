

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
    # Checks if text is empty
    if not text:
        return True

    # Converts text to lowercase and removes all non-alphanumeric characters
    text = text.lower().replace(' ', '')

    # Checks if length of text is 1 or less
    if len(text) <= 1:
        return True

    # Checks if first and last character of text are the same
    if text[0] != text[-1]:
        return False

    # Checks if text length is an even number
    if len(text) % 2 == 0:
        # Iterates over text and checks if it's a palindrome
        for i in range(len(text) // 2):
            if text[i] != text[-i - 1]:
                return False
        return True
    # Iterates over text and checks if it's a palindrome
    for i in range(len(text) // 2):
        if text[i] != text[-i - 1]:
            return False
    return True



