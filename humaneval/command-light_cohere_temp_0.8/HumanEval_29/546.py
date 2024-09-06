```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Unit tests
def test_filter_by_prefix():
    assert filter_by_prefix([], 'a') == ['a']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['abcd', 'cd', 'cde', 'efg'], 'cd') == ['cd']
    assert filter_by_prefix(['apples', 'oranges'], '') == []
test_filter_by_prefix()
``` 
This script defines a function `filter_by_prefix` that filters an input list of strings based on their prefix. 

The function uses a list comprehension to filter out any strings that do not start with the specified prefix. 

The unit tests ensure that the function works correctly for various inputs.