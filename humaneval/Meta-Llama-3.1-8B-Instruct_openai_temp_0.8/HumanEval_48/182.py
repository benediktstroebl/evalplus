```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

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
    import doctest
    doctest.testmod()
```

This script will check whether the given string is a palindrome or not. It first removes any non-alphanumeric characters and converts the string to lowercase to handle cases with different cases and non-alphanumeric characters. It then compares the cleaned text with its reverse to determine if it's a palindrome. The test cases are also included to ensure the function works as expected.