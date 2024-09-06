```python
def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Convert string to list to allow indexing from both sides
    text = list(text)
    # Compare characters from both sides of the list, starting from the middle
    return text[0] == text[-1] and all(text[i] == text[-1-i] for i in range(1, len(text) // 2))
```