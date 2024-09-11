### Palindrome Checker Python Script

```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    A palindrome is a string that reads the same backwards as forwards.

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
    # Remove spaces and convert to lowercase for case-insensitivity
    text = text.replace(" ", "").lower()
    
    # Compare the input string with its reverse
    return text == text[::-1]

# Example usage:
if __name__ == "__main__":
    print(is_palindrome(""))  # True
    print(is_palindrome("aba"))  # True
    print(is_palindrome("aaaaa"))  # True
    print(is_palindrome("zbcd"))  # False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It removes spaces and converts the string to lowercase for case-insensitivity, then compares the input string with its reverse. If they are the same, the function returns `True`; otherwise, it returns `False`. The example usage at the end demonstrates how to use this function.