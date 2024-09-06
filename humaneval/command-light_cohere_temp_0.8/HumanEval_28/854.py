```python
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    Args:
        strings (List[str]): List of strings to concatenate.
    Returns: str: Concatenated string.
    """
    string is a list of any non-empty strings, and joins them with the 
    corresponding strings joined together using the str.
    """
def test_concatenate():
    strings = ['a', 'b', 'c']
    result = concatenate(strings)
    print(result)
    assert result == 'abc'
    return result
```