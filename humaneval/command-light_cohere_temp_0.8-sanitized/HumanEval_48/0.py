def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    :param text: string to check
    :return: boolean value of is palindrome
    """
    return text == text[::-1]