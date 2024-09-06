```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.s if prefix != '' and len(prefix) > 0]

# Test cases
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('x') == []
    assert all_prefixes('') == []
    assert all_prefixes(' ') == ['']
test_all_prefixes()
```
The function all_prefixes takes a string as input and returns a list of all prefixes in the string, excluding the empty string. It uses list comprehension with a generator expression to iterate over the characters in the string, filtering out the prefixes that are not empty and have a non-zero length.