Here's a Python script with a self-contained function that solves the problem of checking if a given text is a palindrome:
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Convert text to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    
    # Check if the reversed text matches the original text
    return text == text[::-1]
```

This script defines a function `is_palindrome` that takes a string text as an argument and returns `True` if it is a palindrome (reads the same forwards and backwards) and `False` otherwise. The function first cleans the input by converting it to lowercase and removing all non-alphanumeric characters using a list comprehension. Then it checks if the cleaned string is equal to its reverse using slicing. The slicing operator `[::-1]` is used to reverse the string without changing the original string.

The docstring explains the purpose of the function and provides informative examples that demonstrate the behaviour of the function for different test cases.