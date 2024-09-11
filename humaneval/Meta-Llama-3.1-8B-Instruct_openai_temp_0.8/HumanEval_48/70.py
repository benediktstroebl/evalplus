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
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. The function first removes non-alphanumeric characters and converts the string to lowercase to make the comparison case-insensitive. It then checks if the cleaned string is equal to its reverse using slicing (`[::-1]`). If they are equal, the function returns `True`; otherwise, it returns `False`.