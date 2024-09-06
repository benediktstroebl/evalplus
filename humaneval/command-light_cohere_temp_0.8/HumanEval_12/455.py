```python
def longest(strings: List[str]) -> Optional[str]:
    return max(strings, key=len, default=None)

# Test cases
strings = ['a', 'b', 'c']
result = longest(strings)
assert result == 'a'  

strings = []
result = longest(strings)
assert result is None 

strings = ['aa', 'bb', 'ccc']
result = longest(strings)
assert result == 'bb' 

strings = ['Python', ' Programming', 'code']
result = longest(strings)
assert len(result) == 9
```