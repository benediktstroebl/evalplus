```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): The input string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """

    # Remove any spaces and convert to lower case to handle cases like "A man, a plan, a canal: Panama"
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()

    # Compare the string with its reverse
    return cleaned_text == cleaned_text[::-1]


# Example use cases
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
print(is_palindrome('A man, a plan, a canal: Panama'))  # True
print(is_palindrome('Not a palindrome'))  # False
```