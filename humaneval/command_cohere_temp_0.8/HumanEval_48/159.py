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

This function leverages string manipulation and the slice notation to check if a given string is a palindrome. It removes all non-alphanumeric characters and converts the string to lowercase to handle cases like 'ABBA' and 'Madam'. The core logic checks if the original string matches its reverse, ensuring efficiency in the process. The provided tests would be helpful in validating the function's behavior.