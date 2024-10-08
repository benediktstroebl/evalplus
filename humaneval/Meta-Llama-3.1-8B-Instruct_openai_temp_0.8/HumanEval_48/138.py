### Palindrome Checker Script
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    
    Args:
    text (str): input string to check
    
    Returns:
    bool: True if string is a palindrome, False otherwise
    
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


# Test cases
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
```
This script defines a function `is_palindrome` that takes a string as input, removes non-alphanumeric characters and converts it to lowercase, and then checks if the cleaned string is equal to its reverse. The script includes test cases to demonstrate the function's behavior.