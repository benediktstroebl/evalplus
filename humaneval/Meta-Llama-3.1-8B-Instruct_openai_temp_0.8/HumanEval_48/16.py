Here's a Python function that checks if a given string is a palindrome:
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

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
    return text.lower() == text.lower()[::-1]

# Example usage:
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
```
In this code, we're using Python's slice notation to reverse the input string, and then comparing it to the original string (both converted to lowercase to make the comparison case-insensitive). This will return `True` if the string is a palindrome and `False` otherwise.

Note that this implementation has a time complexity of O(n), where n is the length of the input string, as it involves creating a reversed copy of the string. However, it's easy to understand and implement, and should be sufficient for most use cases.