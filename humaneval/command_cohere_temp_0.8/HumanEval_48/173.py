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

This `is_palindrome` function checks if a given string is a palindrome, ignoring all non-alphanumeric characters and case. It does this by first cleaning the string by removing all non-alphanumeric characters and converting it to lowercase. Then, it compares the cleaned string with its reverse using slicing (`s[::-1]`) to efficiently reverse the string without using any extra space. It returns `True` if they match, and `False` if they don't.