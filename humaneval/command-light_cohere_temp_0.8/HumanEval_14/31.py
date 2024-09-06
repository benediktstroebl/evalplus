```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(c) for c in string if c != ""]

# Test cases
test_cases = [
    ("abc", ["a", "ab", "abc"]),
    (" ", [""])
]

for test_case in test_cases:
    actual_result = all_prefixes(test_case[0])
    expected_result = test_case[1]
    print(f"Test case: {test_case[0]}, {expected_result}")
    print(f"Actual result: {actual_result}, Expected result: {expected_result}")
    if actual_result != expected_result:
        print("Error in test case!")
    else:
        print("Test case passed!")
```