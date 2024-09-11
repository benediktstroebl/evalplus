### Palindrome Checker Script
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    A palindrome is a string that reads the same backwards as forwards.
    This function is case sensitive and does not remove spaces or punctuation.

    Args:
        text: The string to check.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    return text.lower() == text.lower()[::-1]

# Example usage:
if __name__ == "__main__":
    print(is_palindrome(""))  # True
    print(is_palindrome("aba"))  # True
    print(is_palindrome("aaaaa"))  # True
    print(is_palindrome("zbcd"))  # False
```

In this script, the `is_palindrome` function checks if a string is the same forwards and backwards. The `[::-1]` slice is a common Python idiom for reversing a string. The `lower()` method is used to make the function case-insensitive. The example usage section demonstrates how to use the function with the provided test cases.