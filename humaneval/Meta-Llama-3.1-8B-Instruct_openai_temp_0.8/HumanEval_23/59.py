### Length of a String
#### Problem: Return the length of a given string

Here's a simple Python function to calculate the length of a string:

```python
def strlen(string: str) -> int:
    """
    Return length of given string
    
    Args:
        string (str): Input string
    
    Returns:
        int: Length of the input string
    
    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)

# Test the function
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```

In this code:

*   We define a function `strlen` that takes a string as input and returns its length.
*   We use the built-in `len` function in Python, which returns the number of items in an object.
*   We provide a docstring to explain what the function does, its arguments, return value, and include some examples.
*   Finally, we test the function with some examples to verify its correctness.