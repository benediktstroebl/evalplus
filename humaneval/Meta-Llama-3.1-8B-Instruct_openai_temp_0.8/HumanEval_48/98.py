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


# Test the function
print(is_palindrome(''))  # Expected: True
print(is_palindrome('aba'))  # Expected: True
print(is_palindrome('aaaaa'))  # Expected: True
print(is_palindrome('zbcd'))  # Expected: False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes any non-alphanumeric characters and converts the string to lowercase to ensure the comparison is case-insensitive and ignores non-alphanumeric characters. It then compares the cleaned text with its reverse to determine if it's a palindrome.