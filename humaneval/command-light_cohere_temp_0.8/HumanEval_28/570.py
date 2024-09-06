```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args: strings (List[str]): List of strings to concatenate
    Returns: str: Concatenated string
    """
    return ''.join(strings)

# Test case: Concatenate empty list
print(concatenate([]))
# Output: ""

# Test case: Concatenate list of strings
print(concatenate(['a', 'b', 'c']))
# Output: "abc"
```
This Python code defines a function `concatenate` that takes a list of strings as an argument and concatenates them into a single string. The function uses the string `join` method to apply the concatenation operation. The test cases demonstrate the `concatenate` function's behavior by passing an empty list and a list of strings to the function and printing the resulting concatenated string.