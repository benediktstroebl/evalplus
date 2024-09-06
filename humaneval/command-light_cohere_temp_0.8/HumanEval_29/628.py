```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Testing the filter_by_prefix function with various inputs
test_cases = [
    [], 'a'
    ['abc', 'bcd', 'cde', 'array'], 'a'
    ['hello world', 'hello !', 'hello !here'], 'hello'
]


# Run the test cases and check the results
for case in test_cases:
    assert filter_by_prefix(case, 'a') == case  # Should only contain 'a' and 'array'


print("All tests passed!")
```