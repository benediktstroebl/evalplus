```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string to be checked

    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]


# Example usage:
if __name__ == "__main__":
    print(is_palindrome(''))  # Expected output: True
    print(is_palindrome('aba'))  # Expected output: True
    print(is_palindrome('aaaaa'))  # Expected output: True
    print(is_palindrome('zbcd'))  # Expected output: False
```

This script defines a function `is_palindrome` that takes a string `text` as input, removes non-alphanumeric characters, converts it to lowercase, and checks if the resulting string is equal to its reverse. The example usage at the end demonstrates how to use this function with different inputs.