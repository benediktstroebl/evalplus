```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string to check

    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove any whitespace and convert to lowercase
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Example usage:
if __name__ == "__main__":
    print(is_palindrome(""))  # Expected output: True
    print(is_palindrome("aba"))  # Expected output: True
    print(is_palindrome("aaaaa"))  # Expected output: True
    print(is_palindrome("zbcd"))  # Expected output: False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes any non-alphanumeric characters and converts the string to lowercase to make the check case-insensitive. Then it compares the cleaned string with its reverse to determine if it's a palindrome. The example usage shows how to use the function with different inputs.