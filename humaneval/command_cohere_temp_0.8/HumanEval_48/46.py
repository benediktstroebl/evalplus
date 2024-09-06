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

This `is_palindrome` function takes a string text as input and returns `True` if it is a palindrome (reads the same backwards as forwards) and `False` otherwise. It first removes all non-alphanumeric characters and converts the text to lowercase to make the comparison case-insensitive. Then, it compares the original text with its reverse using slicing (`text[::-1]`) to efficiently reverse the string.