```python
def concatenate(strings: List[str]) -> str:
    """
    Join list of strings into a single string,
    without using any external libraries.
    """

    Parameters:
    strings (List[str]): list of strings to concatenate.
    Returns: joined string.
    """
    string list is
    """ be converted into a string using 'join()'
    """
    return ''.join(strings)

# Test cases
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'

# Run the tests when the script is executed
test_concatenate()
```
This Python code defines a function `concatenate` that joins a list of strings into a single string, without using any external libraries. It uses the non-standard string concatenation method, where the list of strings is converted into a single string using `join()`. reason why string method, which is a self-contained solution that does not require any additional modules or external functions.