```python
def longest(strings: List[str]) -> Optional[str]:
    """
    This function takes a list of strings and returns the length of the longest string in the list.
    Returns None in case that all input strings are empty.
    """
    length of longest element in strings:
    """
    max_length = 0
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
    return max_length if max_length is not 0 else None

# Tests
def test_longest():
    strings = ['a', 'bb', 'ccc']
    assert longest(strings) == 3

def test_empty():
    strings = []
    assert longest(strings) is None

# Run tests
test_longest()
test_empty()
```

This script defines a function called longest that takes a list of strings as input and returns the length of the longest string in the list. The function also returns None if all input strings are empty. The test cases have been added to ensure the function is working correctly.