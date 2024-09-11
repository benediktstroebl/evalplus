```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string to check

    Returns:
        bool: True if the string is a palindrome, False otherwise

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
    return text == text[::-1]

# Test cases
print(is_palindrome(''))  # Expected: True
print(is_palindrome('aba'))  # Expected: True
print(is_palindrome('aaaaa'))  # Expected: True
print(is_palindrome('zbcd'))  # Expected: False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It returns `True` if the string is a palindrome and `False` otherwise. The implementation uses Python's slice notation to reverse the string and compare it with the original string. The test cases at the end demonstrate the function's behavior with different inputs.