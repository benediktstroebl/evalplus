```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(c) for c in string if c != " "]

# Test cases
test_cases = [
    "abc",
    "123",
    "abc123",
    "123456789",
    "hello world"
]

test_results = []

for test_case in test_cases:
    actual_prefixes = all_prefixes(test_case)
    test_results.append(actual_prefixes(actual_prefixes))

def actual_prefixes(prefixes: List[str]) -> List[str]:
    return [prefix[0] for prefix in prefixes]

print("Test Results:", test_results)
```