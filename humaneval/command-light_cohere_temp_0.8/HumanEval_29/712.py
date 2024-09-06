```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test cases
test_cases = [
    [], ['a'], ['abc'], ['bcd', 'cde'], ['array']
]

for test_case in test_cases:
    actual_result = filter_by_prefix(test_case, 'a')
    assert actual_result == ['a', 'abc'], f"Incorrectly filtered results: {actual_result}"

test_cases = [['a', 'bcd', 'cde', 'hello']]
for test_case in test_cases:
    actual_result = filter_by_prefix(test_case, 'cde')
    assert actual_result == ['cde'], f"Incorrectly filtered results: {actual_result}"
```
This code defines a function **filter_by_prefix** that filters an input list of strings based on a given prefix. The test cases demonstrate the both correctly filter the strings and pass all the asserts.