```python
def is_palindrome(text: str):
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
    return text.lower() == text.lower()[::-1]

# Test cases
print(is_palindrome(''))  # Expected output: True
print(is_palindrome('aba'))  # Expected output: True
print(is_palindrome('aaaaa'))  # Expected output: True
print(is_palindrome('zbcd'))  # Expected output: False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It returns `True` if the string is a palindrome and `False` otherwise. The function converts the string to lowercase to make the check case-insensitive and uses slicing (`[::-1]`) to reverse the string. The test cases at the end demonstrate the function's usage.