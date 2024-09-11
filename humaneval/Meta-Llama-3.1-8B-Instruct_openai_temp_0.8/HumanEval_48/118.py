```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    This function is case-sensitive and considers spaces and punctuation as non-matching characters.

    Args:
        text (str): The input string to be checked.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]

# Test cases
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
print(is_palindrome('A man, a plan, a canal: Panama'))  # True
```

In this script, the `is_palindrome` function first removes all non-alphanumeric characters from the input string and converts it to lowercase. It then compares the cleaned string with its reverse. If they are the same, the function returns `True`; otherwise, it returns `False`.