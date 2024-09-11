```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): The input string to check

    Returns:
    bool: True if the input string is a palindrome, False otherwise

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
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Example usage
print(is_palindrome(''))
print(is_palindrome('aba'))
print(is_palindrome('aaaaa'))
print(is_palindrome('zbcd'))
```

This script defines a function `is_palindrome` that takes a string as input, removes any non-alphanumeric characters, and converts it to lowercase. It then checks if the resulting string is equal to its reverse. If they are equal, the function returns `True`, indicating that the input string is a palindrome. Otherwise, it returns `False`.