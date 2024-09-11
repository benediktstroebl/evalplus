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
    # Remove spaces and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]
```

You can run this script in a Python environment to test the `is_palindrome` function. The function works by first cleaning the input string by removing any spaces and converting it to lowercase. It then checks if the cleaned string is equal to its reverse (`cleaned_text[::-1]`). If they are equal, the function returns `True`, indicating that the string is a palindrome. Otherwise, it returns `False`.