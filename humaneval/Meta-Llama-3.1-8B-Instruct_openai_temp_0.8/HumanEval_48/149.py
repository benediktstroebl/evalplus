```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

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
    text = ''.join(c for c in text if c.isalnum()).lower()  # Remove non-alphanumeric characters and convert to lowercase
    return text == text[::-1]  # Check if the string is equal to its reverse

# Test the function
print(is_palindrome(''))
print(is_palindrome('aba'))
print(is_palindrome('aaaaa'))
print(is_palindrome('zbcd'))
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes non-alphanumeric characters and converts the string to lowercase to handle cases where the input string is not a palindrome due to case or non-alphanumeric characters. Then it checks if the resulting string is equal to its reverse, which is done using slicing (`text[::-1]`). The function returns `True` if the string is a palindrome and `False` otherwise. The test cases at the end demonstrate the function's usage.