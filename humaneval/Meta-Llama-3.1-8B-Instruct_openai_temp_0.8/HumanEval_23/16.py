Here is a self-contained Python script that solves the problem:
```markdown
### strlen Function

#### Overview
The `strlen` function returns the length of a given string.

#### Code
```python
def strlen(string: str) -> int:
    """Return length of given string
    
    Args:
        string (str): The input string
    
    Returns:
        int: The length of the input string
    
    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)
```

#### Example Usage
```python
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
print(strlen('Hello, World!'))  # Output: 13
```

#### Notes
* The `strlen` function uses the built-in `len` function in Python to calculate the length of the input string.
* The function takes a string as input and returns an integer representing the length of the string.
* The docstring includes examples to demonstrate the usage of the function.
```