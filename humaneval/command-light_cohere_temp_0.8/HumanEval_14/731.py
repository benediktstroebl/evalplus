```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != ' ' and char != '\n']

# Test cases
test_cases = [
    ("abc", ["a", "ab", "abc"]),
    ("hello world", ["h", "el", "ll", "dlroW"]),
    (" Lorem ipsum dolor sit amet ", ["lo", "rm", "ims", "sd", "amet"])
]

for test_str, expected_result in test_cases:
    actual_result = all_prefixes(test_str)
    print(f"Test case '{test_str}': Expected {'expected_result'}, Actual {'actual_result'}")
    assert actual_result == expected_result
```