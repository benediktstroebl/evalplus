

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
    # if the length of the string is 1 or less than that, it is clearly a palindrome
    if len(text) < 2:
        return True
    
    # initializing two variables with the first and last character
    first_char = text[0]
    last_char = text[-1]
    
    # iterating through the remaining characters and comparing them with the first and last character
    for i in range(1, len(text) - 1):
        if text[i] != first_char:
            return False
    
    # if all characters match with the first and last character, it is a palindrome
    return True