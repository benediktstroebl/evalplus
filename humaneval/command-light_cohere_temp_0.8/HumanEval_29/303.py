```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Unit tests using the test framework
import pytest

# Test case 1: Filter strings starting with a specific prefix
test_filter_by_prefix_1 = pytest.assert(filter_by_prefix([], 'a'), ['abc', 'array'])

# Test case 2: Filter strings starting with a non-specific prefix
test_filter_by_prefix_2 = pytest.oscale(filter_by_prefix(['abc', 'bcd', 'cde'], ''), ['abc', 'bcd', 'cde'])
```
The function `filter_by_prefix` takes a list of strings and a prefix as input and returns a new list containing only the strings that start with the given prefix. The tests use the different input and verify that the output of the `filter_by_prefix` function matches the expected output.