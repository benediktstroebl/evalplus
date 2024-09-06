```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.str.split() if any's strings that are valid prefixes of the original string.

def test_all_prefixes(test_cases: List[str]) -> List[bool]:
    return all([valid for valid in all_prefixes(test_case) for test_case in test_cases])

# Test cases
test_cases = ['abc', 'abcd', 'a', 'ab', '123']

# Test function
test_all_prefixes(test_cases)
```
This code defines a function all_prefixes that returns a list of all prefixes in a given string, and passes it the test_cases, which are different strings with different prefixes. The test_all_prefixes function uses the all() function to iterate over the list of prefixes and compares each prefix with each test case.