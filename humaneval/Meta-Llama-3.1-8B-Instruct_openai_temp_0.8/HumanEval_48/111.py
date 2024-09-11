```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): The input string to check for palindrome

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
print(is_palindrome(""))  # Expected output: True
print(is_palindrome("aba"))  # Expected output: True
print(is_palindrome("aaaaa"))  # Expected output: True
print(is_palindrome("zbcd"))  # Expected output: False
```

This script defines a function `is_palindrome` that checks whether a given string is a palindrome. It achieves this by comparing the input string with its reverse. The `[::-1]` slice notation is used to reverse the string.

The last few lines of the script test the function with the provided examples.