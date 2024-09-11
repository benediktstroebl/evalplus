### Palindrome Checker
#### Problem Description
A palindrome is a string that reads the same backward as forward. This script defines a function to check if a given string is a palindrome.

#### Solution
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome

    Args:
        text (str): The string to check

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
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_text = text.replace(' ', '').lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]
```
#### Example Use Cases
```python
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
print(is_palindrome('Madam'))  # True
print(is_palindrome('Hello'))  # False
```
This script defines a function `is_palindrome` that takes a string `text` as input and returns a boolean indicating whether the string is a palindrome. The function first removes spaces and converts the string to lowercase for case-insensitive comparison. It then compares the cleaned string with its reverse using slicing (`[::-1]`). If they are equal, the function returns `True`, indicating that the string is a palindrome. Otherwise, it returns `False`.