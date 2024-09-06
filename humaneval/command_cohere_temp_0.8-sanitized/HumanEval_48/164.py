def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    :param text: string to be checked
    :return: true if string is palindrome, false otherwise
    """
    # Convert string to lowercase to handle case-insensitive palindromes
    text = text.lower()
    # Check if text is an empty string
    if not text:
        return True
    # Check if last character and first character are the same
    return text[-1] == text[0] and is_palindrome(text[1:-1])