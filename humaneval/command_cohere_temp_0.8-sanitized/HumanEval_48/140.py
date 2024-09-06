def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    :param text: string to be checked
    :return: true if string is palindrome, false otherwise
    """
    # Convert string to lowercase to handle case-insensitive palindromes
    text = text.lower()
    # Check if text is an empty string or has only 1 character
    if len(text) < 2:
        return True
    # Split text into two halves to compare
    half = text[:len(text) // 2]
    return half == text[len(text) // 2:]