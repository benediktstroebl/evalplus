### Palindrome Checker
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    A palindrome is a string that reads the same backwards as forwards.
    The function is case sensitive and considers spaces and punctuation.

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
    return text == text[::-1]


# Test cases
if __name__ == "__main__":
    print(is_palindrome(""))  # Expected output: True
    print(is_palindrome("aba"))  # Expected output: True
    print(is_palindrome("aaaaa"))  # Expected output: True
    print(is_palindrome("zbcd"))  # Expected output: False
```
This script defines a function `is_palindrome` that checks if a given string is a palindrome by comparing it to its reverse. The `[::-1]` slice is used to reverse the string. The function returns `True` if the string is a palindrome and `False` otherwise. The test cases at the end demonstrate the usage of the function.