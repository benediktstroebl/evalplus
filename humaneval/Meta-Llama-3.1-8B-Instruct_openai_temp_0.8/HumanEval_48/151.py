```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): Input string to be checked

    Returns:
    bool: True if string is palindrome, False otherwise
    """
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if __name__ == "__main__":
    print(is_palindrome(''))  # Expected output: True
    print(is_palindrome('aba'))  # Expected output: True
    print(is_palindrome('aaaaa'))  # Expected output: True
    print(is_palindrome('zbcd'))  # Expected output: False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes any non-alphanumeric characters and converts the string to lowercase, then compares the cleaned string with its reverse. If they are the same, the function returns `True`, indicating that the string is a palindrome. Otherwise, it returns `False`. The test cases at the end demonstrate the function's usage and expected output.