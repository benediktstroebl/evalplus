

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
    text_without_spaces = text.replace(' ', '')
    first_half = text_without_spaces[: len(text_without_spaces) // 2]
    second_half = text_without_spaces[len(text_without_spaces) // 2 :]
    return first_half == second_half[::-1]

