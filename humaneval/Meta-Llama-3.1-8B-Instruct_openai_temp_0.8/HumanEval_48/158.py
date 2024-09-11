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
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Example usage:
print(is_palindrome(""))  # True
print(is_palindrome("aba"))  # True
print(is_palindrome("aaaaa"))  # True
print(is_palindrome("zbcd"))  # False
```

This script does the following:

- It defines a function `is_palindrome` that takes a string `text` as an argument.
- It removes any non-alphanumeric characters from the string and converts it to lowercase to handle cases where the string contains upper-case letters or punctuation.
- It then checks if the cleaned string is equal to its reverse (`cleaned_text[::-1]`).
- If the string is equal to its reverse, the function returns `True`, indicating that the original string is a palindrome. Otherwise, it returns `False`.