def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    :param text: String to be checked
    :return: True if string is palindrome, False otherwise
    """
    # Convert string to lowercase to handle case-insensitive palindromes
    text = text.lower()
    # Check if text is empty or has only 1 character, which is a palindrome
    if not text or len(text) == 1:
        return True
    # Check if text is evenly divisible by 2 or not for corner case handling
    if len(text) % 2 == 1:
        return False
    # Count number of characters from start and end moving in opposite directions
    return text[0] == text[-1] and all(text[i] == text[-1-i] for i in range(1, len(text) // 2))