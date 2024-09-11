### Palindrome Checker

Here's a Python script that defines a function to check if a given string is a palindrome.

```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.
    
    Args:
    text (str): The input string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("", True),
        ("aba", True),
        ("aaaaa", True),
        ("zbcd", False),
    ]
    
    for text, expected_result in test_cases:
        result = is_palindrome(text)
        print(f"Test case: {text}, Expected result: {expected_result}, Actual result: {result}")
        assert result == expected_result, f"Test case failed: {text}"
    print("All test cases passed!")
```

### Explanation

The `is_palindrome` function takes a string as input, removes non-alphanumeric characters, converts it to lowercase, and then checks if the resulting string is equal to its reverse.

The test cases cover different scenarios, including an empty string, a palindrome with repeating characters, and a string that is not a palindrome. The `assert` statement is used to verify that the function behaves as expected.

You can run this script to see the test cases pass, indicating that the `is_palindrome` function works correctly.