```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case: filtering strings that contain only 'a'
test_case = ["abc", "bacd", "cde", "array", "a"]
filtered = filter_by_substring(test_case, 'a')
assert filtered == ['abc', 'bacd', 'array']

# Test case: filtering strings that contain 'cde'
test_case = ["abc", "bacd", "cde", "array"]
filtered = filter_by_substring(test_case, 'cde')
assert filtered == []
```