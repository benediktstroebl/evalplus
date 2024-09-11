```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    A palindrome is a string that reads the same backwards as forwards.

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
    # Remove spaces and convert to lowercase to make the comparison case-insensitive
    text = text.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return text == text[::-1]

# Test the function
print(is_palindrome(""))  # Should print: True
print(is_palindrome("aba"))  # Should print: True
print(is_palindrome("aaaaa"))  # Should print: True
print(is_palindrome("zbcd"))  # Should print: False
```

This script defines the `is_palindrome` function, which checks if a given string is a palindrome by removing spaces and converting it to lowercase, and then comparing it with its reverse. The function returns `True` if the string is a palindrome and `False` otherwise. The script also includes example use cases and test cases to demonstrate the function's correctness.