```python
def concatenate(strings: List[str]) -> str:
    """
    Returns the concatenated string of all elements in the input list.
    Args:
        strings (List[str]): A list of strings
    Returns:
        str: The concatenated string of all input strings
    """
    return ''.join(strings)

# Tests
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate(['abc', 'a']) == 'acb'

if __name__ == "__main__":
    test_concatenate()
```
The function concatenate takes a list of strings as input and returns the concatenated string. The tests ensure that function works correctly for empty lists, single strings, and strings with different lengths.