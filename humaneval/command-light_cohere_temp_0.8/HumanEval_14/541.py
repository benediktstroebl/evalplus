Here's a self-contained Python function that returns a list of all prefixes from shortest to longest of an input string:
```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(sorted(string, key=len, reverse=True))

# Test cases
def test_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('abcd') == ['ab', 'ac', 'bd']
    assert all_prefixes('') == []
    assert all_prefixes('x') == ['x']
    assert all_prefixes('abcad') == ['abc', 'acda']

# Run the function and test
test_prefixes()
```

This function utilizes the Python 'sorted' function with the 'key' parameter set to the length of each character and the 'reverse' parameter set to 'True' to ensure proper ordering. The function then returns a list of all prefixes from the shortest character to the longest.