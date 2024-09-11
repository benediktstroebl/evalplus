### Palindrome Checker
#### A Python Script to Check if a Given String is a Palindrome

```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    Args:
    text (str): The input string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.

    Examples:
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    # Remove any spaces and convert to lowercase for accurate comparison
    text = text.replace(" ", "").lower()
    
    # Initialize two pointers, one at the start and one at the end of the string
    left = 0
    right = len(text) - 1
    
    # Compare characters from the start and end, moving towards the center
    while left < right:
        if text[left]!= text[right]:
            return False
        left += 1
        right -= 1
    
    # If the loop completes without finding any mismatches, the string is a palindrome
    return True

# Example usage:
print(is_palindrome(""))  # Expected output: True
print(is_palindrome("aba"))  # Expected output: True
print(is_palindrome("aaaaa"))  # Expected output: True
print(is_palindrome("zbcd"))  # Expected output: False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes any spaces and converts the string to lowercase for accurate comparison. Then, it uses two pointers, one at the start and one at the end of the string, to compare characters from both ends, moving towards the center. If any mismatches are found, the function returns `False`. Otherwise, it returns `True`.