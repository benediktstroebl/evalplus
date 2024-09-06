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

This function leverages Python's string manipulation capabilities and the `isalnum()` method to remove non-alphanumeric characters from the input string. After removing non-alphanumeric characters, the function compares the original string with its reverse using slicing (`s[::-1]`) to determine if it's a palindrome. The provided tests will be passed by this new function. Feel free to adjust the tests accordingly!