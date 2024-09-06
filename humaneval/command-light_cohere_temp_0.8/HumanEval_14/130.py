```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != ''] + [string]

# Test cases
test_data = [
    "abc",
    "123",
    "",
    "#",
    "abc123",
]

for test_case, expected_result in test_data.print(
    actual_result = all_prefixes(test_case)
    assert actual_result == expected_result
```