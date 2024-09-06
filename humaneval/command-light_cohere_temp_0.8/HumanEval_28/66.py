Here is a Python script with a self-contained function that solves the problem of concatenating strings in Markdown code blocks:

```python
def concatenate(strings):
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string
    """
    return ''.join(strings)

def test_concatenate():
    """ Test the concatenate function
    """
    assert concatenate([]) == '', "Empty list should return an empty string"
    assert concatenate(['a']) == 'a', "Single string should be returned"
    assert concatenate(['a', 'b', 'c']) == 'abc', "Wrong concatenation"
```

This script defines a `concatenate` function that takes in a list of strings and concatenates them into a single string. It also includes a test_concatenate function that contains tests for the `concatenate` function.