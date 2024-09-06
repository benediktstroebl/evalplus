def is_palindrome(text: str):
    """
    Checks if a given string is a palindrome.
    """
    # Your code here :)
    text = text.lower()  # Convert to lowercase for case-insensitive comparison
    return text == text[::-1]