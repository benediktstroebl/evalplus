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
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]

# Test cases
if __name__ == "__main__":
    assert is_palindrome('')
    assert is_palindrome('aba')
    assert is_palindrome('aaaaa')
    assert not is_palindrome('zbcd')
    print("All test cases passed")
```

This Python script defines a function `is_palindrome` that checks whether a given string is a palindrome. The function works by first removing any non-alphanumeric characters from the string and converting it to lowercase, then comparing the cleaned string with its reverse. The `is_palindrome` function returns `True` if the string is a palindrome and `False` otherwise. The script also includes test cases to verify the function's correctness.