```python
# Solve the problem:
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    """
    result = ''.join(strings)
    return result

# Run the tests:
def test_concatenate_empty_list():
    assert concatenate([]) == ''

def test_concatenate_non_empty_list():
    assert concatenate(['a', 'b', 'c']) == 'abc'

# Call the tests:
test_concatenate_empty_list()
test_concatenate_non_empty_list()
```