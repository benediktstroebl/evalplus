```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): The input string to be checked.

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
    # Remove whitespace and convert to lowercase for case-insensitive comparison
    text = text.replace(" ", "").lower()
    # Compare the string with its reverse
    return text == text[::-1]

# Example usage:
print(is_palindrome(""))  # True
print(is_palindrome("aba"))  # True
print(is_palindrome("aaaaa"))  # True
print(is_palindrome("zbcd"))  # False
```

This Python function `is_palindrome(text: str)` takes a string as input, removes any whitespace, converts it to lowercase for case-insensitive comparison, and then checks if the resulting string is equal to its reverse. The function returns `True` if the string is a palindrome and `False` otherwise.