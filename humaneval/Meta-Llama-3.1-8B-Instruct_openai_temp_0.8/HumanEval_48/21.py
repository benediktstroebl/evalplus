### Palindrome Checker Script
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The string to check

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


# Example usage:
if __name__ == "__main__":
    print(is_palindrome(""))  # True
    print(is_palindrome("aba"))  # True
    print(is_palindrome("aaaaa"))  # True
    print(is_palindrome("zbcd"))  # False
```
This script defines a function `is_palindrome` that checks if a given string is a palindrome. It uses Python's slicing feature to reverse the string and then compares it to the original string (with all characters converted to lowercase). If the two strings are equal, the function returns `True`; otherwise, it returns `False`. The script includes example usage at the end to demonstrate how to use the function.