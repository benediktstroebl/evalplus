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
    # Remove spaces and convert to lowercase
    clean_text = text.replace(' ', '').lower()
    
    # Compare the string with its reverse
    return clean_text == clean_text[::-1]


# Test the function
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
```

This script defines the `is_palindrome` function which checks if a given string is a palindrome. It first removes any spaces from the string, converts it to lowercase, and then compares it with its reverse. If they are the same, the function returns True; otherwise, it returns False. The script also includes docstrings to describe the function's behavior and provides example use cases.