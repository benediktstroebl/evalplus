Here is a Python script that defines a function all_prefixes which returns a list of all prefixes from shortest to longest of a given string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.full() if prefix else '' ]
# Run some tests on the function
def test():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
```