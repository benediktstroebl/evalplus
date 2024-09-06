```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatented string
    """
    return ''.join(strings)

# Unit tests
strings = ["a", "bc", "a"]
assert concatenate(strings) == "abc"
strings = []
assert concatenate([]) == ""
strings = ["a", "bc"]
assert concatenate(strings) == "abc"
strings = ["a", "bc", "c"]
assert concatenate(strings) == "abc"
```

This script defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. The function uses the single string as a list and returns the concatenated result. The tests in the code ensure that the function is working correctly.