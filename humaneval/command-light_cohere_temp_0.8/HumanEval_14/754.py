```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c != '']

# Test case: Extracting prefixes from 'abc'
test_cases = [
    'abc',
    'abcd',
    # Add more test cases as needed
]

for test_str in test_cases:
    actual_prefixes = all_prefixes(test_str)
    expected_prefixes = ['a', 'ab', 'abc']
    assert actual_prefixes == expected_prefixes, f"Prefixes of '{test_str}': {actual_prefixes} != {expected_prefixes}"
```