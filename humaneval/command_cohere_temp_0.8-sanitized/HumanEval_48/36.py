def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    :param text: string to be checked
    :return: True if string is palindrome, False otherwise
    """
    # Convert string to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    
    # Check if text is same when reading forward and backward
    return text == text[::-1]