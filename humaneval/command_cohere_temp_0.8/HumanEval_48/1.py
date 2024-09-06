```python
def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Convert string to list to allow indexing from both sides
    text = list(text)
    # Compare characters from both sides of the list gradually towards the middle
    return text == text[::-1][:len(text) // 2 + 1 :]
```

This function leverages list indexing and the reversible nature of list slices to efficiently determine whether a string is a palindrome, which is a key aspect of the problem. The empty text case is considered correct as per the problem statement, and the function returns True for empty inputs.