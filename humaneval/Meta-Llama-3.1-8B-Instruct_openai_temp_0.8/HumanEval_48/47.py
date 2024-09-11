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
    # Remove any whitespace and convert to lowercase
    text = text.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return text == text[::-1]


# Test the function
print(is_palindrome(""))  # Expected output: True
print(is_palindrome("aba"))  # Expected output: True
print(is_palindrome("aaaaa"))  # Expected output: True
print(is_palindrome("zbcd"))  # Expected output: False
```

This script defines a function `is_palindrome` that checks whether a given string is a palindrome. It removes any whitespace and converts the string to lowercase to make the comparison case-insensitive. The function then compares the string with its reverse (`text[::-1]`) to determine whether it is a palindrome. Finally, the script tests the function with the provided examples.