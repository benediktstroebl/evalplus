```python
def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Convert string to list to allow indexing from both sides
    temp_list = list(text)
    # Compare characters from both ends of the list until reaching the middle
    return text == ''.join(temp_list[i] for i in range(len(temp_list)//2, -1, -1) if i <= len(temp_list)//2)
```