```python
def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Convert string to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    
    # Check if it is the same forwards and backwards
    return text == text[::-1]
```

This script defines a function, `is_palindrome`, that takes a string as an argument and returns `True` if it is a palindrome (a sequence that reads the same forward and backward) and `False` otherwise. The function first cleans the input by converting it to lowercase and removing all non-alphanumeric characters using a list comprehension. Then, it compares the cleaned string with its reverse using slicing (`slicing ([1:-1])` reverses a sequence) to determine if it's a palindrome.