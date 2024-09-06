```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join("".join(strings))

# Test cases
test_concatenate_cases = [
    [],
    ['a', 'b', 'c'],
    ['a'],
    ['abc', '123']
]

for t in test_concatenate_cases:
    assert concatenate(t) == t[0]
```