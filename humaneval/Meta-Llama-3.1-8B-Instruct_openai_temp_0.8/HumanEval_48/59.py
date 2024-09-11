Here's a self-contained Python script that solves the problem:

```markdown
### Palindrome Checker

A palindrome is a string that reads the same backward as forward.

#### Code

```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The input string

    Returns:
        bool: True if the string is a palindrome, False otherwise

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
```

#### Example Usage

```python
print(is_palindrome(''))  # Output: True
print(is_palindrome('aba'))  # Output: True
print(is_palindrome('aaaaa'))  # Output: True
print(is_palindrome('zbcd'))  # Output: False
```

#### Explanation

1. The function `is_palindrome` takes a string `text` as input.
2. It removes non-alphanumeric characters from the string using a list comprehension and joins the resulting characters into a new string.
3. The cleaned string is converted to lowercase to ensure the function is case-insensitive.
4. The function then compares the cleaned string with its reverse (`text[::-1]`).
5. If the two strings are equal, the function returns `True`, indicating that the original string is a palindrome.
6. Otherwise, it returns `False`.
```