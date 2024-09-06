```python
def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    text = text.lower()  # Convert to lowercase for case-insensitive comparison
    return text == text[::-1]
```

This function compares the input text to its reverse using the slice notation `[::-1]` which reverses a string. It returns True if the text is a palindrome and False if it is not.

To run this function save it in a Python file (e.g., `palindrome_checker.py`) and execute it in your terminal using `python palindrome_checker.py`. You can then call the function with different test cases to verify its behavior.