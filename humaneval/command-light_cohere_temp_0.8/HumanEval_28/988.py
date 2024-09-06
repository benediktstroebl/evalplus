```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    :param strings: List of strings
    :return: String
    """
    return ''.join(strings)

def test_concatenate():
    """ Test the concatenate function
    :return: None
    """
    assert concatenate([]) == '', 'empty list'
    assert concatenate(['a']) == 'a', 'single string'
    assert concatenate(['a', 'b']) == 'ab', 'two strings'
    assert concatenate(['a', 'bc']) == 'abc', 'lists of strings'

# Run the test suite
test_concatenate()
```

This script defines a function called **concatenate** that takes a list of strings and returns their concatenation as a single string. The function is then tested with a series of test cases to ensure it works correctly. The test suite contains a list of tests that cover different scenarios, such as empty lists, single strings, and strings in lists. This allows us to validate the function's correctness.