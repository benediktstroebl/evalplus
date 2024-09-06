```python
def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Convert string to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    
    # Check if the reversed string matches the original string
    return text == text[::-1]
```

This `is_palindrome` function qualifies as self-contained, efficiently determining whether a string is a palindrome without relying on external utilities or excessive code. It normalizes the input by converting it to lowercase and removing non-alphanumeric characters. This ensures that the check for a palindrome is consistent and insensitive to case or non-alphanumeric characters. The core of the check is a simple comparison of the original string with its reverse, making it computationally efficient and suitable for handling various input scenarios.