```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    A palindrome is a string that reads the same backwards as forwards.

    Args:
    text (str): The input string to check

    Returns:
    bool: True if the string is a palindrome, False otherwise
    """
    # Remove any whitespace and convert to lowercase
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
print(is_palindrome(''))  # Expected output: True
print(is_palindrome('aba'))  # Expected output: True
print(is_palindrome('aaaaa'))  # Expected output: True
print(is_palindrome('zbcd'))  # Expected output: False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It removes any non-alphanumeric characters, converts the string to lowercase, and then compares it with its reverse. If they are the same, the string is a palindrome.