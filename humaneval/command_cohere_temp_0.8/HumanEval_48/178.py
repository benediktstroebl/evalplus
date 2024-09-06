Here's a Python script with a self-contained function that solves the problem of checking if a given text is a palindrome:
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

This script defines a function `is_palindrome` that takes a string text as input and returns `True` if it is a palindrome (reads the same forwards and backwards) and `False` otherwise. The function first cleans the input by converting it to lowercase and removing all non-alphanumeric characters using a list comprehension. Then it checks if the cleaned string is equal to its reversed version, using slicing with a negative step indicating reverse.

This function is tested with examples as given in the problem statement to check against an empty string, a multi-word palindrome, and a non-palindrome string.