```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Unit tests using pytest and assert functions
import pytest
import assert

def test_filter():
    assert filter_by_prefix([u for u in 'abc de fgh'.split(), 'a'), ['abc', 'array'])
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'fgh'], 'f'), ['abc', 'fgh']
    assert filter_by_prefix(['abc', 'bcd', 'cde'], 'bcd'), ['abc', 'cde']

# Use the test suite to run the function
pytest.
```
The provided Python script defines a function `filter_by_prefix` that filters a list of strings based on their prefix. It uses the `pytest` and `assert` functions to define a test suite with several assertions. The function takes a list of strings and a prefix as input and returns a new list containing only the strings that start with the given prefix. The test suite ensures that the `filter_by_prefix` function correctly filters the strings based on the given prefix.