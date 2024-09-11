```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    
    Args:
        text (str): Input string to check
    
    Returns:
        bool: True if string is a palindrome, False otherwise
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if __name__ == "__main__":
    print(is_palindrome(""))  # Expected output: True
    print(is_palindrome("aba"))  # Expected output: True
    print(is_palindrome("aaaaa"))  # Expected output: True
    print(is_palindrome("zbcd"))  # Expected output: False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes all non-alphanumeric characters and converts the string to lowercase to make the comparison case-insensitive. It then compares the cleaned string with its reverse. If they are the same, the function returns `True`; otherwise, it returns `False`. The script includes test cases to demonstrate the function's usage.