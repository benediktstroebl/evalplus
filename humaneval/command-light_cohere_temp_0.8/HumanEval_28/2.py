```python
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string
    :param strings: List of strings
    :return: Concatenated string
    """
    return ''.join(strings)

# Test the concatenate function
test_strings = ['a', 'b', 'c']
result = concatenate(test_strings)
assert result == 'abc'
```

This script defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. It uses the then list comprehension to create the concatenated string. The test cases demonstrate that the expected output is 'abc'.