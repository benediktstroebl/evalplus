```python
def concatenate(strings: List[str]) -> str:
    """ Concatenenate list of strings into a single string
    :param strings: list of strings to concatenate
    :type strings: List[str]
    :return: string
    """
    return ''.join(strings)

# Test cases
assert(concatenate([]) == "")
assert(concatenate(['a']) == 'a')
assert(concatenate(['a', 'b', 'c']) == 'abc')
assert(concatenate(['a', 'bb', 'ccc']) == 'abbccc')
```
This code defines a function `concatenate` that takes a list of strings as input and returns the concatenated result as a single string. This is's how it solves the problem and passes the corresponding tests successfully.