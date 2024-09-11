```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): The input string to check

    Returns:
    bool: True if the string is a palindrome, False otherwise
    """
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Example use cases
if __name__ == "__main__":
    print(is_palindrome(""))  # True
    print(is_palindrome("aba"))  # True
    print(is_palindrome("aaaaa"))  # True
    print(is_palindrome("zbcd"))  # False
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It uses a list comprehension with the `isalnum` method to remove all non-alphanumeric characters and the `lower` method to convert the string to lowercase. Then it compares the cleaned text with its reverse using slicing (`[::-1]`). The example use cases demonstrate the function's behavior with different inputs.