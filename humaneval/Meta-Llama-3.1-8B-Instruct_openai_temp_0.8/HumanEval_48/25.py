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
    # Remove spaces and convert to lowercase
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    
    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]


# Example usage:
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
```

In this script, the `is_palindrome` function takes a string as input, removes any non-alphanumeric characters, converts the string to lowercase, and then checks if the resulting string is the same forwards and backwards. If it is, the function returns `True`; otherwise, it returns `False`. The function is then tested with some example inputs to demonstrate its behavior.