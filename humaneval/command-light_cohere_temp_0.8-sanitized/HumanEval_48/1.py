def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    Returns: boolean
    """
    # Remove spaces to make sure only characters are checked
    text = text.replace(' ', '')

    # Convert to lowercase to make the comparison case-insensitive
    return text == text[::-1]