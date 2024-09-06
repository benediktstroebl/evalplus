```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c != '']

# Test cases
test_cases = [
    'abc',
    '123',
    '#12345#',
    'abc123',
    '  ',
    '  abc  '
]

test_results = []

for test_case in test_cases:
    actual_prefixes = all_prefixes(test_case)
    test_results.append(actual_prefixes)

if all(test_results[0] == test_results[1]):
    print("All test cases passed!")
else:
    print("Test case failed.")
```