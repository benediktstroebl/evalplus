```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string to check

    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove whitespace and convert to lowercase
    cleaned_text = text.replace(" ", "").lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]

# Test cases
if is_palindrome(''):
    print("Test case 1: Empty string is a palindrome")
if is_palindrome('aba'):
    print("Test case 2: String 'aba' is a palindrome")
if is_palindrome('aaaaa'):
    print("Test case 3: String 'aaaaa' is a palindrome")
if not is_palindrome('zbcd'):
    print("Test case 4: String 'zbcd' is not a palindrome")
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It removes any whitespace, converts the string to lowercase, and then compares it with its reverse using slicing (`[::-1]`). The test cases at the end demonstrate the function's behavior on different inputs.