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
    # Remove any non-alphanumeric characters and convert to lower case
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
print(is_palindrome('A man, a plan, a canal: Panama'))  # True
print(is_palindrome('Not a palindrome'))  # False
```

This script defines a function `is_palindrome` that takes a string as input and returns `True` if the string is a palindrome and `False` otherwise. The function first removes any non-alphanumeric characters from the string and converts it to lower case, then compares the cleaned string with its reverse. If they are the same, the function returns `True`; otherwise, it returns `False`.