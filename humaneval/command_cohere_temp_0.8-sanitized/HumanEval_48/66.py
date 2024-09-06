def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    :param text: string to be checked
    :return: True if string is palindrome, False otherwise
    """
    # Convert string to lowercase to handle case-sensitive palindrome check
    return text.lower() == text[::-1].lower()