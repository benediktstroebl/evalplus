```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test case 1: Filter strings that start with 'a'
test_case_1 = [ 'abc', 'bcd', 'cde', 'array', 'hello']
test_case_1_expected = ['abc', 'array']

# Test case 2: Filter strings that start with 'ccc'
test_case_2 = ['abc', 'ccc', 'def', 'gjs', 'hello']
test_case_2_expected = ['ccc', 'def', 'gjs']

print(f"Test case 1 passed: {test_case_1_expected}")
print(f"Test case 2 passed: {test_case_2_expected}")
```
The `filter_by_prefix` function filters a list of strings based on a given prefix. It uses the simple Python list comprehension to iterate through the input list of strings. The function then returns a list of strings that start with the given prefix.