```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test case: empty list
test_case_empty = []
result_empty = filter_by_substring(test_case_empty, 'a')
assert result_empty == []

# Test case: list of strings containing the substring
test_case_contains = ['abc', 'bacd', 'cde', 'array']
result_contains = filter_by_substring(test_case_contains, 'a')
assert result_contains == ['abc', 'bacd', 'array']
```

This script provides a self-contained function that filters a list of strings for a given substring, and passes the tests.