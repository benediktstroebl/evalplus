```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string to check

    Returns:
        bool: True if string is a palindrome, False otherwise

    Example:
        >>> is_palindrome('')
        True
        >>> is_palindrome('aba')
        True
        >>> is_palindrome('aaaaa')
        True
        >>> is_palindrome('zbcd')
        False
    """
    text = ''.join(c for c in text if c.isalnum()).lower()  # remove non-alphanumeric characters and convert to lowercase
    return text == text[::-1]  # check if string is equal to its reverse

# Test cases
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes any non-alphanumeric characters from the string and converts it to lowercase, then checks if the resulting string is equal to its reverse. The function returns `True` if the string is a palindrome and `False` otherwise. The script also includes test cases to demonstrate the function's behavior.