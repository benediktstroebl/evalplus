```markdown
### Length of String Function in Python

This script defines a Python function `strlen` to calculate the length of a given string.

#### Code
```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the input string.

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)
```

#### Explanation

The `strlen` function uses the built-in `len` function in Python to calculate the length of the input string. This is a more Pythonic and efficient approach compared to manually counting characters.

#### Example Usage

```python
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
print(strlen('Hello, World!'))  # Output: 13
```

#### Running the Script

To run this script, save it to a file with a `.py` extension (e.g., `strlen.py`) and execute it using Python (e.g., `python strlen.py`).