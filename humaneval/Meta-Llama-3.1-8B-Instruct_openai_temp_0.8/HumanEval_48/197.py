```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    A string is considered a palindrome if it reads the same backward as forward.
    Non-alphanumeric characters and case differences are ignored.
    
    Parameters:
    text (str): The input string to check
    Returns:
    bool: True if the string is a palindrome, False otherwise
    """
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if __name__ == "__main__":
    print(is_palindrome(''))  # True
    print(is_palindrome('aba'))  # True
    print(is_palindrome('aaaaa'))  # True
    print(is_palindrome('zbcd'))  # False
    print(is_palindrome('A man, a plan, a canal: Panama'))  # True
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome. It first removes non-alphanumeric characters and converts the string to lowercase to ignore case differences. It then compares the cleaned string with its reverse to determine if it's a palindrome. The test cases at the end demonstrate the function's usage.