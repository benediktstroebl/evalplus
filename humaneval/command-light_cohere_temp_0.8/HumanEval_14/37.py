```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [str for str in string if str else '']

# Test the function with various inputs
test_cases = [
    "abc",
    "abc123",
    "",
    "a",
    "Hello World",
    "qpww Reboulme",
]

for test_case in test_cases:
    actual_result = all_prefixes(test_case)
    expected_result = [str(i) for i in test_case if i]
    assert actual_result == expected_result, f"Test case '{test_case}' failed."
```