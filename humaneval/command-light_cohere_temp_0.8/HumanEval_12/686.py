```python
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    max_length = max(len(string) for string in strings)
    return max(strings)[:max_length]

# Test cases
strings = ['a', 'b', 'c']
result = longest(strings)
assert result == 'a'

strings = ['aa', 'bb', 'ccc']
result = longest(strings)
assert result == 'bb'ccc'

strings = []
result = longest(strings)
assert result is None
```