```python
def concatenate(strings: List[str]) -> str:
    return ''.join(strings)

# Test cases
assert concatenate([]) == ''
assert concatenate(['a']) == 'a'
assert concatenate(['a', 'b']) == 'ab'
assert concatenate(['a', 'b', 'c']) == 'abc'

# Correct output: 'abc'
```
This code defines a function `concatenate` that takes a list of strings and returns the concatenated string. The test cases ensure that function works correctly with empty lists, single strings, and multiple strings.