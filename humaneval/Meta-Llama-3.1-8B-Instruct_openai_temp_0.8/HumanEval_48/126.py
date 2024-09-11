```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    A palindrome is a string that reads the same backwards as forwards.

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]

# Example usage:
print(is_palindrome(''))  # Should print: True
print(is_palindrome('aba'))  # Should print: True
print(is_palindrome('aaaaa'))  # Should print: True
print(is_palindrome('zbcd'))  # Should print: False
```