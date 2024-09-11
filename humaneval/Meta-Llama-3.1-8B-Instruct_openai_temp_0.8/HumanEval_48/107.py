## Palindrome Checker
### A Python Script to Check if a Given String is a Palindrome

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
    # Remove any leading or trailing whitespace and convert to lowercase
    text = text.strip().lower()
    
    # Compare the text with its reverse
    return text == text[::-1]


# Example usage:
print(is_palindrome(""))  # True
print(is_palindrome("aba"))  # True
print(is_palindrome("aaaaa"))  # True
print(is_palindrome("zbcd"))  # False
```

This script defines a function `is_palindrome` that takes a string as input, removes any leading or trailing whitespace, converts it to lowercase, and then checks if the resulting string is equal to its reverse. The function returns `True` if the string is a palindrome and `False` otherwise. The examples at the end demonstrate the function's usage.