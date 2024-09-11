```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    A palindrome is a string that reads the same backwards as forwards.
    This function ignores case, punctuation and whitespace.

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
    text = ''.join(e for e in text if e.isalnum()).lower()
    return text == text[::-1]


# Example usage
print(is_palindrome(""))  # True
print(is_palindrome("aba"))  # True
print(is_palindrome("aaaaa"))  # True
print(is_palindrome("zbcd"))  # False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes all non-alphanumeric characters from the string and converts it to lowercase. Then it checks if the resulting string is equal to its reverse. If they are equal, the function returns `True`; otherwise, it returns `False`. The script includes some example usage to demonstrate how the function works.