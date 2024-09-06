def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Convert text to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    
    # Check if the reversed text matches the original text
    return text == text[::-1]