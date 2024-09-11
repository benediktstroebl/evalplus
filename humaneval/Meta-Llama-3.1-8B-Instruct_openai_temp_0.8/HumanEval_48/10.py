```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    
    A palindrome is a string that reads the same backwards as forwards.
    This function is case-sensitive and does not remove whitespace.
    
    Parameters:
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

# Example usage
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
```

In this code, the `is_palindrome` function checks if the input string `text` is the same when reversed. It uses Python's slicing feature to create a reversed copy of the string (`text[::-1]`) and then compares it to the original string. If they are the same, the function returns `True`, indicating that the string is a palindrome. Otherwise, it returns `False`.