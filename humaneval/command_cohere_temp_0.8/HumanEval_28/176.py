```python
# Solve the problem:
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    """
    result = ''
    for string in strings:
        result += string
    return result

# Run the tests:
def test_concatenate_empty_list():
    """ Test empty list case """
    assert concatenate([]) == ''

def test_concatenate_non_empty_list():
    """ Test non-empty list case """
    assert concatenate(['a', 'b', 'c']) == 'abc'

# Run the tests
test_concatenate_empty_list()
test_concatenate_non_empty_list()
```