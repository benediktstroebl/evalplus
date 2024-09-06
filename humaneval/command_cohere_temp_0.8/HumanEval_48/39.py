```python
def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Convert string to list to allow indexing from both sides
    text = list(text)
    # Check if text is equal to its reverse
    return text == text[::-1]
```