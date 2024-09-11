```markdown
### Flip Case Function

Below is a Python function that flips the case of a given string.

```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string to flip the case.

    Returns:
        str: The string with its case flipped.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.lower() if char.isupper() else char.upper() for char in string)
```

### Usage

```python
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('HELLO'))  # Output: 'hELLO'
print(flip_case('hello'))  # Output: 'HELLO'
```

This function uses a generator expression to iterate over each character in the input string. If the character is uppercase (`isupper()` returns `True`), it converts it to lowercase using `lower()`. Otherwise, it converts the lowercase character to uppercase using `upper()`. The `join()` function then concatenates these characters back into a single string.