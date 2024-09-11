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
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]

# Test the function
print(is_palindrome(''))  # Expected: True
print(is_palindrome('aba'))  # Expected: True
print(is_palindrome('aaaaa'))  # Expected: True
print(is_palindrome('zbcd'))  # Expected: False
```

In this script, the `is_palindrome` function uses a list comprehension to remove any non-alphanumeric characters from the input string, and then converts it to lowercase. It then compares the cleaned text with its reverse, which is obtained using slicing (`text[::-1]`). If the two are equal, the function returns `True`, indicating that the input string is a palindrome. Otherwise, it returns `False`.