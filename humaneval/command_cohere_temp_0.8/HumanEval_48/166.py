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

This `is_palindrome` function checks if a given text is a palindrome. It removes all non-alphanumeric characters and converts the text to lowercase to ensure a case-insensitive match. Then, it compares the original text with its reverse to determine if it's a palindrome.