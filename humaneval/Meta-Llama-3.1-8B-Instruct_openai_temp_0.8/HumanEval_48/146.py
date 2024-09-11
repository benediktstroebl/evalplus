```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): The input string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Remove any non-alphanumeric characters and convert to lower case
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

This script will test the `is_palindrome` function with the provided test cases using the `doctest` module. The function itself works by removing any non-alphanumeric characters from the input string, converting it to lower case, and then comparing it with its reverse. If they are the same, the function returns `True`; otherwise, it returns `False`.