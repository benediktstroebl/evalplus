```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test cases for the function
test_strings = [
    ['abc', 'bcd', 'cde', 'a', 'arO', 'spa'],
    ['abc', 'bb', 'ccc'],
    ['hello world'],
    ['array', 'a', 'price'],
    ['']

test_prefix = 'a'

expected_result = ['abc', 'array']

test_cases = [test_strings, test_prefix, test_prefix]

for case in test_cases:
    actual_result = filter_by_prefix(case, test_prefix)
    assert actual_result == expected_result, "Test case failed: {} != {}"
```