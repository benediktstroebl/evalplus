Here's a Python script with a self-contained function that solves the problem of checking if a given text is a palindrome:
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    
    Args:
        text (str): Text to be checked.
    
    Returns:
        bool: True if the text is a palindrome, False otherwise.
    """
    # Convert text to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    
    # Check if the reversed text matches the original text
    return text == text[::-1]
```
This function uses a few powerful string methods:
- `isalnum()` to check if each character is alphanumeric (letters or digits).
- `lower()` to convert the entire string to lowercase.
- `join()` to reconstruct a cleaned string from the filtered characters.

Then, it simply compares the original text with its reverse to determine if it's a palindrome. This solution provides an informative docstring, adheres to PEP 8 conventions, and solves the problem efficiently.