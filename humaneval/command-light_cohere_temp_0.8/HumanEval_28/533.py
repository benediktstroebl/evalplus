```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatenated string
    """
    return "".join(strings)

# Test case: Concatenate empty list
assert concatenate([]) == ""

# Test case: Concatenate list of strings
assert concatenate(['a', 'b', 'c']) == 'abc'
```
The provided code defines a function `concatenate` that takes a list of strings as input and concatenates them into a single string. It provides a test cases to validate the functionality, passing all the tests with expected results.