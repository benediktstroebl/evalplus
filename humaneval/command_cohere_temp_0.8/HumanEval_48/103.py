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
This function uses a combination of string methods and indexing to achieve this in a straightforward manner.

To use this function, you can simply call it with a string as an argument:
```python
>>> is_palindrome('aba')
True
>>> is_palindrome('aaaaa')
True
>>> is_palindrome('zbcd')
False
```

This script effectively solves the problem and passes the tests outlined in the original prompt.