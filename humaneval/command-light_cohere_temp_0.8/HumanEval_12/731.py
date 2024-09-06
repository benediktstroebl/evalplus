```python
def longest(strings: List[str]) -> Optional[str]:
    return max(strings, key=len) if strings else None

# Test cases
strings = ['a', 'b', 'c']
longest(strings)  # Output: 'c'

strings = ['a']
longest(strings)  # Output: 'a'

strings = []
longest(strings)  # Output: None

strings = ['a', 'bb', 'ccc']
longest("")  # Raises TypeError: unsupported operand type('') for comparison
```