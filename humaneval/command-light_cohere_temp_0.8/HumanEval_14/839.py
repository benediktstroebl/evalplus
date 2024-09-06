```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.string() if prefix.isalpha()]
 string. shorter_prefixes = string.isalpha()
 shortest_prefix = min(string.isalpha(), shorter_prefixes)
    return [shortest_prefix] + all_prefixes(shortest_prefixes)

# Test cases
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('hello world') == ['hello', 'hl', 'llow']
```