```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.

    Args:
    text (str): The string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned string with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if __name__ == "__main__":
    print(is_palindrome(""))  # Expected: True
    print(is_palindrome("aba"))  # Expected: True
    print(is_palindrome("aaaaa"))  # Expected: True
    print(is_palindrome("zbcd"))  # Expected: False
```

In this script, we define a function `is_palindrome` that takes a string `text` as input. It first removes all non-alphanumeric characters from the string and converts it to lowercase to make the palindrome check case-insensitive. Then, it checks if the cleaned string is equal to its reverse. If they are equal, the original string is a palindrome, and the function returns `True`. Otherwise, it returns `False`.

The test cases at the end of the script demonstrate the function's behavior with different inputs.