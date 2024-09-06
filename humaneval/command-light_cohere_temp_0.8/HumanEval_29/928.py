```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Unit tests for the filter_by_prefix function
def test_filter_by_prefix():
    assert filter_by_prefix([], 'a') == ['a']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['abcd', 'bcde', 'cdef'], 'b') == ['bcde', 'cdef']
    assert filter_by_prefix(['cdef', 'a', 'cdef'], 'c') == ['cdef']
    assert filter_by_prefix(['a', 'bcde'], 'bcd') == []
```
The script defines a function `filter_by_prefix` that filters an input list of strings based on their prefix. It then has various tests to validate this function's correctness, ensuring it returns the expected results for different inputs.