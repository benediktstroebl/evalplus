```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The string to check.

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
    text = ''.join(e for e in text if e.isalnum()).lower()  # Remove non-alphanumeric characters and convert to lower case
    return text == text[::-1]  # Compare the string with its reverse


# Test cases
if __name__ == "__main__":
    print(is_palindrome(""))  # True
    print(is_palindrome("aba"))  # True
    print(is_palindrome("aaaaa"))  # True
    print(is_palindrome("zbcd"))  # False
```
This script defines a function `is_palindrome` that takes a string as input, removes non-alphanumeric characters, and checks if the resulting string is equal to its reverse. The function returns `True` if the string is a palindrome, and `False` otherwise. The script also includes test cases to demonstrate the function's behavior.