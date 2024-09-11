```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string to check

    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]


# Example usage:
if __name__ == "__main__":
    assert is_palindrome('')  # True
    assert is_palindrome('aba')  # True
    assert is_palindrome('aaaaa')  # True
    assert not is_palindrome('zbcd')  # False
    print("All assertions passed!")
```

This script provides a function `is_palindrome` that checks if a given string is a palindrome by removing non-alphanumeric characters, converting to lowercase, and comparing the resulting string with its reverse. The example usage demonstrates how to use the function with the provided test cases.