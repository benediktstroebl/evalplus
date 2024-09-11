```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

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
    return text == text[::-1]  # Check if the string is equal to its reverse


# Example usage:
if __name__ == "__main__":
    print(is_palindrome(""))  # True
    print(is_palindrome("aba"))  # True
    print(is_palindrome("aaaaa"))  # True
    print(is_palindrome("zbcd"))  # False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes any non-alphanumeric characters and converts the string to lowercase to handle cases where the palindrome appears to be case-sensitive. The function then checks if the resulting string is equal to its reverse, which is a common way to determine if a string is a palindrome. If the string is equal to its reverse, the function returns `True`, otherwise it returns `False`. The example usage section demonstrates how to use the `is_palindrome` function with different inputs.