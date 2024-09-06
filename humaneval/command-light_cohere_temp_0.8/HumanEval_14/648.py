```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != '']

# Test cases
test_cases = [
    'abc',
    '123',
    '',
    '#!/bin',
]

test_results = []
for test_case in test_cases:
    actual_prefixes = all_prefixes(test_case)
    test_results.append(actual_prefixes)  # List comprehension for easy append

print("Test Results:")
for result, actual in zip(test_results, actual_prefixes):
    print(f"{result}: {actual}")
```