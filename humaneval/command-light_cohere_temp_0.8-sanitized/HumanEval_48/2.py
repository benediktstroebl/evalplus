def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    Return True if the string is a palindrome, otherwise False
    """
    return text == text[::-1] or text == text[::-1][::-1]