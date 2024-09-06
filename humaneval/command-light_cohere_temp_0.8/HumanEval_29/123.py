```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Unit tests for the filter_by_prefix function
def test_filter_by_prefix():
    assert filter_by_prefix([], 'a') == ['a']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['abc', 'b', 'cde'], 'a') == ['abc']
    assert filter_by_prefix(['array', 'cde', 'axpt'], 'a') == ['array']
``` 

This code defines a function **`filter_by_prefix`** which filters an input list of strings based on a given prefix. The function uses the filtering technique to accept any input list of strings and any valid prefix. The test_filter_by_prefix function evaluates the filter_by_prefix function with various inputs and compares the result against the expected output, ensuring that the function works as expected.