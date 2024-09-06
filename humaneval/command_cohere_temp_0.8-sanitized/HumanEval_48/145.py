def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Convert string to list to allow indexing from both sides
    text = list(text)
    # Compare characters from both sides of the list gradually towards the middle
    return text == text[::-1][:len(text) // 2 + 1 :]