```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Unit tests
test_filter_by_prefix = []
test_filter_by_prefix.push_one('abc')
test_filter_by_prefix.push_one('a')
test_filter_by_prefix.push_one('add')
test_filter_by_prefix.push_one('array')

def test():
    assert filter_by_prefix(test_strings, 'a') == ['abc']
    assert filter_by_prefix(test_strings, 'add') == ['add']

def test_filter_by_prefix():
    test_filter_by_prefix()
```
The problem is to filter an input list of strings only for ones that start with a given prefix.  The function uses the filter, which is a list comprehension that iterates through the input list of strings.