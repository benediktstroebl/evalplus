```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings (List[str]): List of strings to concatenate

    Returns:
    str: Concatenated string
    """
    return ''.join(strings)

# Test case: Concatenate empty list
print(concatenate([]))  # Output: ""

# Test case: Concatenate list of strings
print(concatenate(['a', 'b', 'c']))  # Output: "abc"
```
This script defines a function `concatenate` that takes a list of strings as an argument and concatenates them into a single string.

The function uses the `join` method to concatenate the strings, and the tests pass the output of the function with different input lists.