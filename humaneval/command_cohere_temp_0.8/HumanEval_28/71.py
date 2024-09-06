```python
# Solve the problem:
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    """
    result = ''.join(strings)
    return result

# Run the tests:
def test_concatenate_list_empty():
    """ Test empty list case """
    assert concatenate([]) == ''

def test_concatenate_list_non_empty():
    """ Test non-empty list case """
    assert concatenate(['a', 'b', 'c']) == 'abc'

# Run the tests
test_concatenate_list_empty()
test_concatenate_list_non_empty()
```

This script includes the `concatenate` function that takes a list of strings and returns a single string. It blanks out the empty list. It joins the list of strings together with spaces using the `join` method. 

It also includes two test functions (`test_concatenate_list_empty` and `test_concatenate_list_non_empty`) that check the function behavior against specific cases:
- `test_concatenate_list_empty` checks if the function returns an empty string for an empty list.
- `test_concatenate_list_non_empty` checks if the function concatenates strings as expected for a non-empty list. 

To run the tests, you can add the line `test_concatenate_list_empty()`, and `test_concatenate_list_non_empty()` at the end of the script, and execute the script either through your IDE or command line. Otherwise, you can remove the test blocks if you only want to keep the `concatenate` function.