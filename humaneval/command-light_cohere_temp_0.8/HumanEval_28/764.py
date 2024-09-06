Here is a Python script with a self-contained function that solves the problem of concatenating strings:
```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate  
    Returns:
        str: Concatenated string
    """
    return ''.join(strings)

# Example usage
strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result) # Output: 'abc'
```

This script defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. The function uses the basic Python string concatenation `join` method with the strings list. The example usage demonstrates how to use the function and concatenate the strings list to 'abc'.