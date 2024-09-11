```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): The input string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if is_palindrome(''):
    print("Tests passed.")
else:
    print("Test failed for empty string.")
if is_palindrome('aba'):
    print("Tests passed.")
else:
    print("Test failed for palindrome.")
if is_palindrome('aaaaa'):
    print("Tests passed.")
else:
    print("Test failed for palindrome with repeating characters.")
if not is_palindrome('zbcd'):
    print("Tests passed.")
else:
    print("Test failed for non-palindrome.")
```

This script defines a function `is_palindrome` that takes a string as input, removes non-alphanumeric characters, converts the string to lowercase, and checks if the cleaned string is equal to its reverse. The `[::-1]` slice notation is used to reverse the string. The test cases are included to demonstrate the function's correctness.