```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): Input string to check

    Returns:
    bool: True if string is a palindrome, False otherwise

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
print(is_palindrome(""))  # Expected: True
print(is_palindrome("aba"))  # Expected: True
print(is_palindrome("aaaaa"))  # Expected: True
print(is_palindrome("zbcd"))  # Expected: False
```

This script defines a function `is_palindrome` that checks if a given string `text` is a palindrome by comparing it with its reverse (`text[::-1]`). The `[::-1]` syntax in Python is used to reverse a string. The function returns `True` if the string is a palindrome and `False` otherwise. The test cases at the end demonstrate how to use this function.