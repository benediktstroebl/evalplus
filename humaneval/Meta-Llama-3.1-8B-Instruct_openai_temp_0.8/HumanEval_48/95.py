```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): Input string to check.

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


# Example usage:
print(is_palindrome(""))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes any spaces from the string and converts it to lowercase for case-insensitive comparison. Then it compares the string with its reverse. If they are the same, the string is a palindrome and the function returns `True`, otherwise it returns `False`. The function includes docstrings with examples to demonstrate its usage.