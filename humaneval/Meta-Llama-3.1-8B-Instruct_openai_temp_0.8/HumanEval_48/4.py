**Palindrome Checker**
======================

Here's a Python script that implements a function to check if a given string is a palindrome:

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
    text = ''.join(e for e in text if e.isalnum()).lower()  # Remove non-alphanumeric characters and convert to lowercase
    return text == text[::-1]  # Compare the string with its reverse

# Example usage:
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
```

In this code:

1. The `is_palindrome` function takes a string `text` as input.
2. It removes non-alphanumeric characters from the string and converts it to lowercase to handle cases with special characters or different cases.
3. It checks if the resulting string is equal to its reverse (`text[::-1]`).
4. If they are equal, the function returns `True`, indicating that the string is a palindrome. Otherwise, it returns `False`.