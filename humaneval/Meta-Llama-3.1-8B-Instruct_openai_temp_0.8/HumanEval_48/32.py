### Palindrome Checker Script
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): The input string to check

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
    # Remove whitespace and convert to lowercase for case-insensitive comparison
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]
```

### Example Usage:
```python
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It removes whitespace and converts the string to lowercase for case-insensitive comparison. The function then checks if the cleaned string is equal to its reverse. If they are equal, the function returns `True`, indicating that the string is a palindrome. Otherwise, it returns `False`. The script includes example usage to demonstrate the function's behavior.