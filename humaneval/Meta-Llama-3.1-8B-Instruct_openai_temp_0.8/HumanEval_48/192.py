```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

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
    # Remove spaces and convert to lowercase to ignore case sensitivity
    text = ''.join(e for e in text if e.isalnum()).lower()
    
    # Compare the string with its reverse
    return text == text[::-1]

# Test cases
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
```

This Python function works as follows:

- It first removes all non-alphanumeric characters from the input string and converts it to lowercase to ignore case sensitivity.
- It then compares the resulting string with its reverse (`text[::-1]`). If they are equal, the function returns True, indicating that the string is a palindrome. Otherwise, it returns False.