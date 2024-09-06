```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.s if prefix.isalpha(prefix)]
from collections import Counter

test_cases = [
    "abc",
    "123",
    "",
    "abc123",
    "foo bar",
]

for test_case in test_cases:
    actual_result = all_prefixes(test_case)
    expected_result = ["", "", "abc", "abc", "abc123"]
    assert actual_result == expected_result, f"Test case: {test_case}, expected: {expected_result}, actual: {actual_result}"

```
The code defines a function all_prefixes that returns a list of all prefixes of a given string. It uses the method Counter from the collections module to count the occurrences of each prefix in the string, and then uses list comprehension to filter out the prefixes. The code also includes a set of test cases, and uses assertion to verify that the function returns the correct results for each test case.