```markdown
### Palindrome Checker
#### A Python Script to Check if a Given String is a Palindrome

```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome('')
        True
        >>> is_palindrome('aba')
        True
        >>> is_palindrome('aaaaa')
        True
        >>> is_palindrome('zbcd')
        False
    """
    # Remove spaces and convert to lowercase
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Example usage
if __name__ == "__main__":
    test_cases = ['', 'aba', 'aaaaa', 'zbcd']
    for test_case in test_cases:
        print(f"Is '{test_case}' a palindrome? {is_palindrome(test_case)}")
```

This script defines a function `is_palindrome` that takes an input string, removes spaces and non-alphanumeric characters, and converts it to lowercase. It then checks if the cleaned string is the same when reversed. The function returns `True` if the string is a palindrome and `False` otherwise.

The script also includes example usage, where it tests the function with a list of test cases and prints the results.