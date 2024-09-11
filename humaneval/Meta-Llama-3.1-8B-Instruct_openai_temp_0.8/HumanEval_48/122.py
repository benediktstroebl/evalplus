```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string to be checked

    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove any whitespace and convert to lowercase
    cleaned_text = ''.join(c for c in text if c.isdigit() or c.isalpha()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Example use cases
if __name__ == "__main__":
    print(is_palindrome(''))  # True
    print(is_palindrome('aba'))  # True
    print(is_palindrome('aaaaa'))  # True
    print(is_palindrome('zbcd'))  # False
    print(is_palindrome('A man, a plan, a canal: Panama'))  # True
```

This script defines a function `is_palindrome` that takes a string as input, removes any whitespace and digits, converts it to lowercase, and checks if it's equal to its reverse. The example use cases demonstrate the function's behavior with different inputs.