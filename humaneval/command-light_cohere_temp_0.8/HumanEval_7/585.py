Here is a self-contained Python script that includes the function `filter_by_substring` that solves the problem of filtering an input list of strings for ones that contain a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain the substring """
    return [s for s in strings if s.find(substring)]


# Test cases
test_cases = [
    [],
    ['abc', 'bacd', 'cde', 'array'],
    ['']
]

for test_case in test_cases:
    actual_result = filter_by_substring(test_case, 'a')
    print(f'Expected: {', list(map(str.find, test_case)))
    print(f'Actual: {', actual_result)}')
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list of strings that contain the substring. The script then provides a list of test cases to test the function, and prints the expected and actual results for each test case.