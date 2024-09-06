Here is a self-contained Python function that solves the problem of finding the longest string in a list of strings:
```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string from the list.
    Args:
    strings (list of str): list of strings

    Returns:
    str or None: the longest string
    """
    if not strings:
        return None

    # Initialize and return the first string in the list
    return max(strings, key=len)

# Unit tests
def test_longest():
    assert longest(['a', 'b', 'c']) == 'a'
    assert longest(['aa', 'bb', 'ccc']) == 'ccc'
    assert longest([]) == None
```
This code defines a function `longest` that takes a list of strings as input and returns the longest string. It uses the tested to find the longest string in the list, with various input combinations, and ensures it works correctly.