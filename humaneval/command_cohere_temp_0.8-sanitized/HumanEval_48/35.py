def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Convert string to list to allow reversed iterating
    text_list = list(text)
    # Compare each character from beginning to end and return boolean result
    return text_list == text_list[::-1()]