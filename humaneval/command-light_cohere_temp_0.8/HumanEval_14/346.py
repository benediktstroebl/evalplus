```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [i for i in string if i]
# Test cases
test_cases = [
    "abc",
    "123",
    "hello world!",
    "",
    " ",
    "1234",
    "abc123"
]

for test_case in test_cases:
    actual_result = all_prefixes(test_case)
    expected_result = [i for i in test_case if i]
    print(f"Test case: {test_case}")
    print("Actual:", actual_result)
    print("Expected:", expected_result)
    print("="*(len(str(actual_result))+1))
    print()
```