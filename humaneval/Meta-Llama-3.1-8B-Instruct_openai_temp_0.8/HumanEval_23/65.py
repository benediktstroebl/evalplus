```python
def strlen(string: str) -> int:
    """
    Return length of given string
    
    Parameters:
    string (str): The input string
    
    Returns:
    int: The length of the input string
    
    Examples:
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    # Use built-in len() function to get the length of the string
    return len(string)

# Test the function
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```
This script defines a function `strlen` that takes a string as input and returns its length. The function uses the built-in `len()` function to calculate the length of the string. The docstring provides a description of the function, its parameters, and its return value, as well as some examples of how to use it. The script also includes some test cases to demonstrate the function's behavior.