```python
def concatenate(strings: List[str]) -> str:
    """ Concatenenate list of strings into a single string
    :param strings: list of strings
    :return: string
    """
    return ''.join(strings)

# Tests
strings = ['a', 'b', 'c']
result = concatenate(strings)
assert result == 'abc'
strings = []
result = concatenate(strings)
assert result == ''
```
This code defines a function **concatenate** that takes a list of strings as an argument and returns the concatenation of these strings as a single string. The tests ensure that code works correctly and passes all the test cases.