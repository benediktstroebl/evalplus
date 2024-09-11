```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

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
    # Remove spaces and convert to lowercase for case-insensitive comparison
    text = text.replace(' ', '').lower()
    
    # Compare the string with its reverse
    return text == text[::-1]


# Test the function
print(is_palindrome(''))  # Expected output: True
print(is_palindrome('aba'))  # Expected output: True
print(is_palindrome('aaaaa'))  # Expected output: True
print(is_palindrome('zbcd'))  # Expected output: False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It removes spaces and converts the string to lowercase for case-insensitive comparison, then checks if the resulting string is equal to its reverse. The `[::-1]` syntax is used to get the characters of the string in reverse order. The function returns `True` if the string is a palindrome and `False` otherwise. Finally, the script includes some test cases to demonstrate the function's behavior.