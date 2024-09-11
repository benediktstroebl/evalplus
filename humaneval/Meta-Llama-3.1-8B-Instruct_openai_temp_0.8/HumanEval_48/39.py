```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): Input string to check

    Returns:
        bool: True if string is a palindrome, False otherwise
    """
    # Remove whitespace and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare string with its reverse
    return cleaned_text == cleaned_text[::-1]

# Example usage:
print(is_palindrome(""))  # True
print(is_palindrome("aba"))  # True
print(is_palindrome("aaaaa"))  # True
print(is_palindrome("zbcd"))  # False
```

This script defines a function `is_palindrome` that takes a string `text` as input and returns `True` if it is a palindrome, and `False` otherwise. It uses a list comprehension to remove non-alphanumeric characters from the string and convert it to lowercase, then checks if the cleaned string is the same when reversed.