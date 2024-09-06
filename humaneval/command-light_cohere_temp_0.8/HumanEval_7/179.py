Here is a Python script with a self-contained function that solves the problem of filtering an input list of strings for ones that contain a given substring:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]

# Test case 1: Filter empty list
test_case1 = []
result1 = filter_by_substring(test_case1, 'a')
assert result1 == []

# Test case 2: Filter list with one string containing substring
test_case2 = ['abc']
result2 = filter_by_substring(test_case2, 'a')
assert result2 == ['abc']

# Test case 3: Filter list with multiple strings containing substring
test_case3 = ['abc', 'bacd', 'cde', 'array']
result3 = filter_by_substring(test_case3, 'a')
assert result3 == ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that filters an input list of strings and returns a new list containing only the strings that contain the given substring. It also provides a testing cases to ensure the function's correctness.