```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    Args:
    text (str): The input string to be checked.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Example usage
print(is_palindrome(''))  # Expected output: True
print(is_palindrome('aba'))  # Expected output: True
print(is_palindrome('aaaaa'))  # Expected output: True
print(is_palindrome('zbcd'))  # Expected output: False
```

This script defines a function `is_palindrome` that takes a string as input, removes any non-alphanumeric characters, and checks if the resulting string is equal to its reverse. The function returns `True` if the string is a palindrome and `False` otherwise. The example usage at the end demonstrates the function's behavior with the provided test cases.