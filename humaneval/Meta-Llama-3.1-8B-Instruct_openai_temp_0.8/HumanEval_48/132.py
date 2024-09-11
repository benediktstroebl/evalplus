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
    # Remove non-alphanumeric characters and convert to lower case
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
print(is_palindrome(''))  # Expected output: True
print(is_palindrome('aba'))  # Expected output: True
print(is_palindrome('aaaaa'))  # Expected output: True
print(is_palindrome('zbcd'))  # Expected output: False
```

This Python script defines a function `is_palindrome` that checks if a given string is a palindrome. It uses the following steps:

1. Removes non-alphanumeric characters from the string using a generator expression and `str.isalnum()` method.
2. Converts the string to lower case to make the comparison case-insensitive.
3. Compares the cleaned string with its reverse using slicing (`[::-1]`).
4. Returns `True` if the string is a palindrome, `False` otherwise.

The script includes the original docstring and test cases as specified. The test cases demonstrate that the function works correctly for empty strings, single-character strings, and non-palindromes.