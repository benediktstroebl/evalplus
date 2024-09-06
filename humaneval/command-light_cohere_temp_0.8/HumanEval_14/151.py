```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != '']

#Test cases
test_cases = [
    ("abc", ["a", "ab", "abc"]),
    ("abcde", ["abcde"]),
    ("abcdefghijklmnopqr", ["abcdefghijklmnop"]),
    ("", []),
    ("123", []),
]

for test_str, expected_result in test_cases:
    actual_result = all_prefixes(test_str)
    print(f"Test '{test_str}' - Expected: {expected_result}, Actual: {actual_result}")
``` 
This code defines a function all_prefixes that returns a list of prefixes from the shortest to the longest, considering only non-alphanumeric characters. It uses the also tests the passed to the function and printed, to verify that the function is working correctly.