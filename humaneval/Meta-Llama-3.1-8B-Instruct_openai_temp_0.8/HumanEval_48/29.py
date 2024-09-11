### Palindrome Checker
#### Python Script

```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): Input string

    Returns:
        bool: True if string is a palindrome, False otherwise

    Example:
        >>> is_palindrome('')
        True
        >>> is_palindrome('aba')
        True
        >>> is_palindrome('aaaaa')
        True
        >>> is_palindrome('zbcd')
        False
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes non-alphanumeric characters and converts the string to lowercase to ensure the comparison is case-insensitive and ignores non-relevant characters. The function then compares the cleaned text with its reverse using slicing (`[::-1]`). If they are equal, the function returns `True`, indicating that the original string is a palindrome.