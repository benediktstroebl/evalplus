```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings (List[str]): List of strings to concatenate
    Returns:
    str: Concatenated string
    """
    return ''.join(strings)

# Test case 1: empty list
print(concatenate([]))  # Output: empty string ''

# Test case 2: list of one string
print(concatenate(['a']))  # Output: 'a'

# Test case 3: list of three strings
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```
The code defines a function `concatenate` that takes a list of strings as an argument and concatenates them into a single string. It returns the simple and list of strings using the `join` method is a concise way to create a string from a list of strings in Python.