def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Convert string to list to allow iteration from both ends
    text = list(text)
    # Compare characters from both ends of the list sequentially
    return text == text[::-1]