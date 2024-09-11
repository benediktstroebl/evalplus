```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string to check

    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    
    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if __name__ == "__main__":
    print(is_palindrome(''))  # Expected output: True
    print(is_palindrome('aba'))  # Expected output: True
    print(is_palindrome('aaaaa'))  # Expected output: True
    print(is_palindrome('zbcd'))  # Expected output: False
```

This Python script defines a function `is_palindrome` that checks if a given string is a palindrome. The function removes spaces and converts the string to lowercase for case-insensitive comparison. It then compares the cleaned string with its reverse using Python's slice notation (`[::-1]`). If they are the same, the function returns `True`; otherwise, it returns `False`. The script includes test cases to demonstrate the function's behavior.