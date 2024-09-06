```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a' + c for c in string]

# Test the function with different inputs
test_cases = [
    'abc',
    'abc123',
    '',
    ']'
]

for test_str in test_cases:
    actual_result = all_prefixes(test_str)
    expected_result = ['', 'ab', 'abc', 'abc123']
    print(f"Test case '{test_str}": actual result: {actual_result}, expected result: {expected_result}")
```