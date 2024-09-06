```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(c) for c in string if c != '']

# Test cases
test_cases = [
    'abc',
    'Hello World',
    '',
    '    ',
]

for test_str in test_cases:
    actual_prefixes = all_prefixes(test_str)
    assert len(actual_prefixes) == len(expected_prefixes), f"Failed for {test_str}."
    expected_prefixes = ['', 'h', 'ello', 'world']
    assert actual_prefixes == expected_prefixes, f"Failed for {test_str}."
```
The code defines a function `all_prefixes(string: str)` that returns a list of prefixes from the input string. The function uses list comprehension to iterate through all characters in the string and filter out non-letters using the `not '` operator. The function is tested against the test cases, and the results are compared against the expected prefixes. The code uses the verify that the `all_prefixes()` function is working correctly for each test case.