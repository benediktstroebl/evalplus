### Checking for Palindromes in Python

Here's a Python function to solve the problem:

```markdown
### is_palindrome.py

```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    A palindrome is a string that reads the same backwards as forwards.

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
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char for char in text if char.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


if __name__ == "__main__":
    # Test cases
    print(is_palindrome(""))  # Expected output: True
    print(is_palindrome("aba"))  # Expected output: True
    print(is_palindrome("aaaaa"))  # Expected output: True
    print(is_palindrome("zbcd"))  # Expected output: False
```

### Explanation:

*   The function `is_palindrome` takes an input string `text`.
*   It removes all non-alphanumeric characters from the text and converts it to lowercase to make the comparison case-insensitive.
*   Then, it checks if the cleaned text is the same when its characters are reversed. This is done using Python's slicing feature (`[::-1]`).
*   If the text is the same when reversed, the function returns `True`, indicating that the input string is a palindrome. Otherwise, it returns `False`.

### Running the script:

You can run this script directly in your Python environment, and it will execute the test cases at the end. Alternatively, you can save this script to a file named `is_palindrome.py` and run it using `python is_palindrome.py`.