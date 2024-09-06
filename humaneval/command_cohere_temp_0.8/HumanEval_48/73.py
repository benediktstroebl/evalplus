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

This `is_palindrome` function uses a couple of clever tricks to achieve good performance:
1. It converts the input string to lowercase and removes all non-alphanumeric characters. This reduces the complexity of the problem by ignoring spaces, punctuation, and capitalization.
2. It uses slicing (`text[::-1]`) to reverse the string without using the `reversed` function, which is slower for long strings due to its O(n) time complexity.

This approach provides a efficient solution with a time complexity of O(n) for determining if a string is a palindrome.