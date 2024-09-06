```python
def longest(strings: List[str]) -> Optional[str]:
    return max(strings, key=len)

# Tests
strings = ['a', 'b', 'c']
strings. longest()
assert longest(strings) == 'c', "Expected longest string not found"

# Test with empty list
strings = []
empty_strings = longest([''])
assert empty_strings is None, "Expected None for empty list"

# Test with one string
strings = ['a']
assert longest(strings) == 'a', "Expected longest string not found"

# Test with list of different lengths
strings = [['a', 'b', 'c', 'd'])
assert longest(strings) == 'c', "Expected longest string not found"
```