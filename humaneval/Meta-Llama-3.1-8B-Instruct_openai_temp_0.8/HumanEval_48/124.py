```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    A palindrome is a string that reads the same backwards as forwards.

    Args:
    text (str): The input string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if __name__ == "__main__":
    print(is_palindrome(''))  # Expected output: True
    print(is_palindrome('aba'))  # Expected output: True
    print(is_palindrome('aaaaa'))  # Expected output: True
    print(is_palindrome('zbcd'))  # Expected output: False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It does this by removing any non-alphanumeric characters and converting the string to lowercase, then comparing the cleaned string with its reverse. The function returns `True` if the string is a palindrome and `False` otherwise. The script includes test cases to demonstrate its usage.