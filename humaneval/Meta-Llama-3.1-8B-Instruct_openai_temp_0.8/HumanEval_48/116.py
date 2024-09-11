```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
    text (str): The input string to be checked

    Returns:
    bool: True if the string is a palindrome, False otherwise
    """
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if __name__ == "__main__":
    print(is_palindrome(""))  # True
    print(is_palindrome("aba"))  # True
    print(is_palindrome("aaaaa"))  # True
    print(is_palindrome("zbcd"))  # False
```

In this script, the `is_palindrome` function takes a string as input, removes any non-alphanumeric characters, and converts it to lowercase. It then checks if the cleaned string is equal to its reverse. If they are equal, the function returns True, indicating that the string is a palindrome; otherwise, it returns False. The test cases at the end of the script demonstrate the function's behavior with different inputs.