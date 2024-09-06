def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Convert string to list to allow reverse traversal
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]