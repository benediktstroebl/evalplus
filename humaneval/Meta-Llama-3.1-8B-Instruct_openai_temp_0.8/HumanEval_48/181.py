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
    # Remove any spaces and convert to lowercase
    text = text.replace(' ', '').lower()
    
    # Compare the input string with its reverse
    return text == text[::-1]
```

You can run this script in your Python environment to test the function. It defines a function `is_palindrome` that takes a string as input, removes any spaces, converts it to lowercase, and checks if the resulting string is equal to its reverse. If they are equal, the function returns `True`; otherwise, it returns `False`.