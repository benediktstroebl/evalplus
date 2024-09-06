```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatenated string
    """
    return ''.join(strings)

# Test the function
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```
This code defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. The function uses the simple list comprehension to concatenate the strings and return the result as a single string. This code is simple and efficient, and it passes the tests successfully.