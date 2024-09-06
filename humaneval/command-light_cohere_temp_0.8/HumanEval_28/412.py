```python
from typing import List
def concatenate(strings: List[str]) -> str:
    return ''.join(strings)

# Test cases
test_concatenate_cases = [
    [],    ""
    ["a"], "b"
    ["a", "b", "c"]
]

for test_case in test_concatenate_cases:
    actual_result = concatenate(test_case)
    expected_result = test_case
    print(f"Test case: { actual, expected } -> { actual, expected })
```