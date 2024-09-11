### Palindrome Checker
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
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]

# Test cases
if __name__ == "__main__":
    print(is_palindrome(''))  # Expected: True
    print(is_palindrome('aba'))  # Expected: True
    print(is_palindrome('aaaaa'))  # Expected: True
    print(is_palindrome('zbcd'))  # Expected: False
```

This script defines a function `is_palindrome` that checks whether a given string is a palindrome. It first removes non-alphanumeric characters and converts the string to lowercase to handle case-insensitivity and non-alphanumeric characters. Then, it compares the cleaned text with its reverse using slicing (`[::-1]`). If they are equal, the function returns `True`, indicating that the string is a palindrome; otherwise, it returns `False`. The test cases at the end demonstrate the function's behavior with different inputs.