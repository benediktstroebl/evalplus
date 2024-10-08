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
if is_palindrome(''):
    print("is_palindrome('') = True")
if is_palindrome('aba'):
    print("is_palindrome('aba') = True")
if is_palindrome('aaaaa'):
    print("is_palindrome('aaaaa') = True")
if not is_palindrome('zbcd'):
    print("is_palindrome('zbcd') = False")
```

This script defines the `is_palindrome` function, which checks if a given string is a palindrome. It first removes any non-alphanumeric characters and converts the text to lowercase to ensure the comparison is case-insensitive. The function then checks if the cleaned text is equal to its reverse. The test cases at the end demonstrate the function's behavior with different inputs.