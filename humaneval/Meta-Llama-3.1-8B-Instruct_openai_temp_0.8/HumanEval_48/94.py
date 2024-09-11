```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    A palindrome is a string that reads the same backwards as forwards.
    CASE-SENSITIVE and PUNCTUATION-SENSITIVE.

    Args:
        text (str): Input string to check

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
    return text == text[::-1]


# Test cases
if __name__ == "__main__":
    print(is_palindrome("")) # Expected: True
    print(is_palindrome("aba")) # Expected: True
    print(is_palindrome("aaaaa")) # Expected: True
    print(is_palindrome("zbcd")) # Expected: False
```

This script uses Python's slice notation to reverse the input string and then checks if it's equal to the original. This approach is efficient, readable, and adheres to the problem's requirements. The code is also documented with a docstring that explains the purpose, behavior, and usage of the `is_palindrome` function.