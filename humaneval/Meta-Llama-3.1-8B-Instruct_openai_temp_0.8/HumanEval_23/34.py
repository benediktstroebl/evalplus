```python
def strlen(string: str) -> int:
    """
    Returns the length of the given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the input string.
    """
    # Use the built-in len() function in Python to get the length of the string
    return len(string)

# Test cases
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```

This Python script defines a function `strlen` that takes a string as input and returns its length using the `len()` function. The function is then tested with two example cases: an empty string and a string with three characters. The output of the script matches the expected results from the docstring.