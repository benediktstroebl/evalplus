```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test case: filter strings that start with 'c'
test_case = [
    'cc', 'ced', 'cat', 'cart', 'cell', 'circle'
]
result = filter_by_prefix(test_case, 'c')
assert result == ['cc', 'ced', 'cat', 'cart', 'cell', 'circle'], "Error: Wrong result"

# Test case: filter strings with empty string
test_case2 = ['cd', 'r', '', 'center', 'cell']
result2 = filter_by_prefix(test_case2, 'c')
assert result2 == ['cd'], "Error: Empty prefix is not filtered"

# Test case: filter strings with only digits
test_case3 = ['abc123', '35']
result3 = filter_by_prefix(test_case3, ' ')
assert result3 == ['123', ''], "Error: Non-string prefix is not filtered"

print("All tests passed!")
```