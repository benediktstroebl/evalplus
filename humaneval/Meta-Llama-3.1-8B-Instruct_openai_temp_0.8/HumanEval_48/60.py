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
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()

    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It does this by first removing non-alphanumeric characters and converting the string to lowercase, then comparing the resulting string with its reverse. The function returns `True` if the string is a palindrome and `False` otherwise. The docstring provides examples of how to use the function.