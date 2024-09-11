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
    # Remove any spaces and convert to lowercase for case insensitive comparison
    text = text.replace(' ', '').lower()
    
    # Compare the string with its reverse
    return text == text[::-1]
```

You can run this script and test the function with different inputs to see its output.