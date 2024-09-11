```python
def is_palindrome(text: str):
    """
    Checks if given string is a palindrome.
    
    A string is considered a palindrome if it reads the same backwards as forwards.
    
    Args:
        text (str): The input string to check.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove any spaces and convert to lowercase for case-insensitive comparison
    cleaned_text = text.replace(' ', '').lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]

# Test cases
if __name__ == "__main__":
    assert is_palindrome('')  # True
    assert is_palindrome('aba')  # True
    assert is_palindrome('aaaaa')  # True
    assert not is_palindrome('zbcd')  # False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It removes any spaces, converts the string to lowercase, and then compares it with its reverse. The result is returned as a boolean value.

The script also includes test cases to verify the function's correctness.