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
    # Remove spaces and convert to lowercase for case-insensitive comparison
    text = text.replace(' ', '').lower()
    
    # Compare the input string with its reverse
    return text == text[::-1]


# Test the function
if __name__ == "__main__":
    print(is_palindrome(""))  # Expected output: True
    print(is_palindrome("aba"))  # Expected output: True
    print(is_palindrome("aaaaa"))  # Expected output: True
    print(is_palindrome("zbcd"))  # Expected output: False
```

This script defines a function `is_palindrome` that takes a string as input and returns `True` if the string is a palindrome and `False` otherwise. It removes spaces from the input string, converts it to lowercase for case-insensitive comparison, and then checks if the resulting string is equal to its reverse. The reverse of a string can be obtained in Python using slicing with a step of -1 (`[::-1]`). The script also includes a test section at the end to demonstrate the function's behavior with different inputs.