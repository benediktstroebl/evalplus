```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Unit tests for filter_by_prefix function
def test_filter_by_prefix():
    assert filter_by_prefix([], 'a') == ['a']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['x', 'y', 'z'], 'xy') == []
test_filter_by_prefix()
```
This code defines a function called `filter_by_prefix`, which filters an input list of strings and returns a new list that includes only those that start with a given prefix. It uses the same testing to ensure that the function behaves correctly.