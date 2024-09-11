```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string to check

    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]

# Test cases
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first cleans the string by removing any non-alphanumeric characters and converting it to lowercase. Then it compares the cleaned string with its reverse. If they are the same, the function returns `True`; otherwise, it returns `False`. The test cases at the end demonstrate the function's behavior with different inputs.