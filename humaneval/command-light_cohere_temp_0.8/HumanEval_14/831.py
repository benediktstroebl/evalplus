```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != ' ']

# Test cases
def test_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']

def test_prefixes2():
    assert all_prefixes('xx') == []

def test_prefixes3():
    assert all_prefixes('') == []
```
The script defines a function all_prefixes that returns a list of prefixes from the input string, removing any spaces. It also includes test cases to test the functionality.