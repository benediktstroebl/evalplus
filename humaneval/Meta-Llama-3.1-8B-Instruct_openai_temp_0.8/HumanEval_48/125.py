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
    # Remove whitespace and convert to lowercase
    text = ''.join(e for e in text if e.isalnum()).lower()
    
    # Compare the string with its reverse
    return text == text[::-1]


# Test the function
print(is_palindrome(''))  # Expected output: True
print(is_palindrome('aba'))  # Expected output: True
print(is_palindrome('aaaaa'))  # Expected output: True
print(is_palindrome('zbcd'))  # Expected output: False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes any non-alphanumeric characters and converts the string to lowercase to ensure the comparison is case-insensitive and ignores spaces and punctuation. It then compares the string with its reverse, using Python's slice notation `text[::-1]`. If the string is equal to its reverse, the function returns `True`; otherwise, it returns `False`. The script includes docstrings and example use cases to demonstrate the function's behavior.