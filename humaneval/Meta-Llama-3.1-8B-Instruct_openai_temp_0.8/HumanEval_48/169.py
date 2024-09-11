```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.
    
    A string is considered a palindrome if it reads the same backward as forward.
    
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
    # Remove any spaces and convert to lowercase for comparison
    text = text.replace(' ', '').lower()
    
    # Compare the string with its reverse
    return text == text[::-1]
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes any spaces and converts the string to lowercase to ensure the comparison is case-insensitive. Then it compares the string with its reverse using slicing (`text[::-1]`). If the string is the same when reversed, it returns `True`, indicating the string is a palindrome. Otherwise, it returns `False`.