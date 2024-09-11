```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

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
    text = text.replace(" ", "").lower()
    # Compare the string with its reverse
    return text == text[::-1]


# Test cases
print(is_palindrome(''))  # Expected output: True
print(is_palindrome('aba'))  # Expected output: True
print(is_palindrome('aaaaa'))  # Expected output: True
print(is_palindrome('zbcd'))  # Expected output: False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes any spaces from the string and converts it to lowercase to make the comparison case-insensitive. Then it compares the string with its reverse using Python's slicing feature. If they are the same, the function returns `True`, indicating that the string is a palindrome. Otherwise, it returns `False`. The script also includes test cases to demonstrate the function's correctness.