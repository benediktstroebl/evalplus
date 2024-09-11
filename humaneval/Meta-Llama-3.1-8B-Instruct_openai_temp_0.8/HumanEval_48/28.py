```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    
    Args:
    text (str): The input string to be checked.
    
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
    
    # Remove any white spaces and convert the string to lowercase
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    
    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test the function
if __name__ == "__main__":
    print(is_palindrome(""))  # Should print: True
    print(is_palindrome("aba"))  # Should print: True
    print(is_palindrome("aaaaa"))  # Should print: True
    print(is_palindrome("zbcd"))  # Should print: False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes any non-alphanumeric characters and converts the string to lowercase to make the comparison case-insensitive. It then compares the cleaned string with its reverse. If they are the same, the function returns `True`; otherwise, it returns `False`. The script includes test cases to demonstrate the function's behavior.