```python
def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string in the list, or None if empty.
    """
   
    list must be a list of strings.
    return max(strings, key=len)

# Test cases
strings = ['a', 'bb', 'ccc']
assert longest(strings) == 'ccc'

strings = ['a']
assert longest(strings) == 'a'

strings = []
assert longest(strings) is None

strings = ['a', 'bb', 'ccc']
assert longest(strings) == 'bb'

strings = ['aa', 'b', 'b', 'ccc']
assert longest(strings) == 'b'
```

The code defines a function `longest` that takes a list of strings as input and returns the longest string. It uses the `max` function along with `key=len` to find the longest string.