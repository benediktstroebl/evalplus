Here's a Python script with a self-contained function that solves the problem of checking if a given string is a palindrome:
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

This `is_palindrome` function first prepares the input by removing non-alphanumeric characters and converting the string to lowercase to ensure a case-insensitive comparison. It then compares the original string with its reverse to determine if it's a palindrome.