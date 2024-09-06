```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join("".join(string[i:])) for i in range(0, len(string), 1)]

# Test cases
test_cases = [
    'abc',
    'Hello World',
    '123',
    '',
    ' '
]

test_results = {}

for test_case in test_cases:
    actual_prefixes = all_prefixes(test_case)
    expected_prefixes = ['', 'h', 'ello ', '1', '12', '123']
    test_results[test_case] = actual_prefixes == expected_prefixes

print(test_results)
```