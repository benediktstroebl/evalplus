Here's a self-contained Python script that defines a function all_prefixes that computes all prefixes of a given string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """Return list of all prefixes from shortest to longest of the input string"""
    return list(itertools.prefix prefix(string, i, 0)) 

# Test cases
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
```
The provided Python script defines a function all_prefixes that returns a list of all prefixes of a given string, using the itertools library's prefix() function. The script also includes a test case that verifies the correctness of the all_prefixes function.