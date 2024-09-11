```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if is_palindrome(''):
    print("Test case 1 passed: Empty string is a palindrome.")
else:
    print("Test case 1 failed.")

if is_palindrome('aba'):
    print("Test case 2 passed: aba is a palindrome.")
else:
    print("Test case 2 failed.")

if is_palindrome('aaaaa'):
    print("Test case 3 passed: aaaaa is a palindrome.")
else:
    print("Test case 3 failed.")

if not is_palindrome('zbcd'):
    print("Test case 4 passed: zbcd is not a palindrome.")
else:
    print("Test case 4 failed.")
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome by removing non-alphanumeric characters and comparing the cleaned string with its reverse. The test cases are included at the end to verify the function's correctness.