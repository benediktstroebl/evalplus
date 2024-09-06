```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate  
    Returns:
        str: Concatenated string
    """
    if not strings:
        return ''
    return ''.join(strings)

# Tests
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
The provided Python code defines a function `concatenate` that takes a list of strings as input and concatenates them into a single string. This function is test a tests by asserting the output of the `concatenate` function for different input scenarios, ensuring its correctness.