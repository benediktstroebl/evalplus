```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.string() if prefix.startswith(string)]

# Test cases
test_cases = [
    'abc',
    'hello world', 
    'abcdefghijklmnopqr',
    '122 123 456-789',
    # Add more tests as needed
]

assert all_prefixes('abc') == ['a', 'ab', 'abc']
assert all_prefixes('hello world') == ['hello', 'world']
assert all_prefixes('abcdefghijklmnopqr') == ['abcdefghijklmnopqr']
assert all_prefixes('122 123 456-789') == ['122', '123', '456-789']

print("All tests passed!")
```