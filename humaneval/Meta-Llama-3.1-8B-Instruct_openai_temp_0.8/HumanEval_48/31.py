### Palindrome Checker
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): The string to check for palindrome

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
    return text.lower() == text.lower()[::-1]

# Test cases
print(is_palindrome(""))  # True
print(is_palindrome("aba"))  # True
print(is_palindrome("aaaaa"))  # True
print(is_palindrome("zbcd"))  # False
```
This script defines a function `is_palindrome` that checks if a given string is a palindrome. It uses Python's slicing feature to reverse the string and then compares it to the original string (converted to lowercase to make the check case-insensitive). If they are the same, the function returns `True`; otherwise, it returns `False`. The test cases at the end demonstrate this function's behavior.