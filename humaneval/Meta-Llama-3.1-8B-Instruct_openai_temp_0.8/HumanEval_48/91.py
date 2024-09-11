### Palindrome Checker
```markdown
### Description
A palindromic string reads the same backwards as forwards. This script defines a function `is_palindrome` to check if a given string is a palindrome.

### Code
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): Input string

    Returns:
    bool: True if string is a palindrome, False otherwise

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
### Explanation
This script defines a function `is_palindrome` that takes a string input `text` and returns a boolean value indicating whether the string is a palindrome. The function converts the input string to lowercase to make the comparison case-insensitive, and then checks if the string is equal to its reverse (`[::-1]` is Python's slice notation for reversing a string). If the string is equal to its reverse, it is a palindrome, and the function returns `True`. Otherwise, it returns `False`.