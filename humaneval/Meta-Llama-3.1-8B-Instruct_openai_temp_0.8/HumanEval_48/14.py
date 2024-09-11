### Palindrome Checker
#### A Python Script to Check if a Given String is a Palindrome

```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    Args:
        text (str): The input string to be checked.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove spaces and convert to lowercase
    text = text.replace(' ', '').lower()
    
    # Compare the string with its reverse
    return text == text[::-1]


# Example use cases
if __name__ == "__main__":
    print(is_palindrome(""))  # Expected output: True
    print(is_palindrome("aba"))  # Expected output: True
    print(is_palindrome("aaaaa"))  # Expected output: True
    print(is_palindrome("zbcd"))  # Expected output: False
```

In this script, the `is_palindrome` function takes a string as input, removes any spaces, converts it to lowercase, and then checks if it's equal to its reverse. The `[::-1]` syntax is used to reverse the string. The example use cases demonstrate the function's behavior with different inputs.