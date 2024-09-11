```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

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
    return text == text[::-1]


# Test cases
if __name__ == "__main__":
    assert is_palindrome("")
    assert is_palindrome("aba")
    assert is_palindrome("aaaaa")
    assert not is_palindrome("zbcd")
```

This script defines a function `is_palindrome` that checks if a given string is equal to its reverse. The function uses Python's slicing feature to reverse the string (`text[::-1]`). The script includes docstrings to provide documentation and examples of usage. The test cases at the end ensure the function behaves as expected for different input scenarios.