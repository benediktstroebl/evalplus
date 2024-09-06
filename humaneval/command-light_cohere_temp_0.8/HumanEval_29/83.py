```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Unit tests using the test framework
import pytest

# Testing function using the filter_by_prefix function
def test_filter_by_prefix():
    assert filter_by_prefix([], 'a') == ['a']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['11', '22', '33'], '21') == []

# Run the tests
pytest.org
```