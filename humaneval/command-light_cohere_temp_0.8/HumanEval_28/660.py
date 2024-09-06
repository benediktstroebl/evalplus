```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatenated string
    """
    return ''.join(strings)

# Test
strings = ['a', 'b', 'c']
print(concatenate(strings))  # Output: 'abc'
```
The solution is a single Python string that is created by passing a list of strings into the `concat` function. The result also passes the example tests.