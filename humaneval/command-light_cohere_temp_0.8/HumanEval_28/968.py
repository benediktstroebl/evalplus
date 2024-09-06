```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    :param strings: List of strings to concatenate
    :return: Concatenated string
    """
    return ''.join(strings)

# Test cases
assert concatenate([]) == ''
assert concatenate(['a']) == 'a'
assert concatenate(['a', 'b']) == 'ab'
assert concatenate(['a', 'b', 'c']) == 'abc'
```
This code defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. It uses the specific testing in the code to ensure the correctness of the function.