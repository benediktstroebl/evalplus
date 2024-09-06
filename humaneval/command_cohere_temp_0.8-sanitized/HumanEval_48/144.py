def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Split the text into individual characters
    text = text.strip()
    return text == text[::-1]