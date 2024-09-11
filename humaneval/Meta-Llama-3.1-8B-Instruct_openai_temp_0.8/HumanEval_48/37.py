### Palindrome Checker Script
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.
    
    Args:
        text (str): The input string.
    
    Returns:
        bool: True if string is a palindrome, False otherwise.
    
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
if __name__ == "__main__":
    print(is_palindrome(""))  # Expected output: True
    print(is_palindrome("aba"))  # Expected output: True
    print(is_palindrome("aaaaa"))  # Expected output: True
    print(is_palindrome("zbcd"))  # Expected output: False
```
In this script, the `is_palindrome` function checks if the input string is a palindrome by comparing the string with its reverse (achieved using slicing with a step of -1). The comparison is case-insensitive due to the use of `text.lower()`. The function also includes a docstring with examples and a clear description of its functionality.