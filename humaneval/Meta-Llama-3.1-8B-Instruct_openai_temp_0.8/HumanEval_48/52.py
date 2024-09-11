```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): Input string to check

    Returns:
    bool: True if string is a palindrome, False otherwise
    """
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("", True),
        ("aba", True),
        ("aaaaa", True),
        ("zbcd", False),
    ]

    for text, expected_output in test_cases:
        result = is_palindrome(text)
        print(f"Test case: {text}, Expected: {expected_output}, Actual: {result}")
        assert result == expected_output, f"Test case '{text}' failed"
    print("All test cases passed!")
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It removes any non-alphanumeric characters and converts the string to lowercase before checking if it's a palindrome by comparing it with its reverse. The script also includes test cases to verify that the function works correctly.