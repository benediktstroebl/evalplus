```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome('')
        True
        >>> is_palindrome('aba')
        True
        >>> is_palindrome('aaaaa')
        True
        >>> is_palindrome('zbcd')
        False
    """
    # Remove spaces and convert to lowercase to ignore case sensitivity
    cleaned_text = text.replace(" ", "").lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]

# Example usage:
print(is_palindrome(""))  # Expected output: True
print(is_palindrome("aba"))  # Expected output: True
print(is_palindrome("aaaaa"))  # Expected output: True
print(is_palindrome("zbcd"))  # Expected output: False
```

This script uses Python's slice notation (`[::-1]`) to reverse the input string, and then compares it with the cleaned string (which has had spaces removed and is in lowercase). The `is_palindrome` function returns `True` if the string is the same when reversed, and `False` otherwise.