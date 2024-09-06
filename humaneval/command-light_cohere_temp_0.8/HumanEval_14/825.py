```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(c) for c in string if c != ' ']
def test_prefixes():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
def test_prefixes_empty():
    assert all_prefixes("") == []
def test_prefixes_special():
    assert all_prefixes("hello world!") == ['h', 'll', 'og', 'wrld']
```
This script provides a self-contained function and tests for checking all prefixes in a given input string.