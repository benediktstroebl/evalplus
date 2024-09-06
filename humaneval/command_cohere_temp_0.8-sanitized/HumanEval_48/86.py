def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    :param text: string to be checked
    :return: boolean
    """
    # Convert text to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    return text == text[::-1]