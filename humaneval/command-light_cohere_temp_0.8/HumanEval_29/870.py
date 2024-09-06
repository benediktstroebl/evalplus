```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test cases
test_cases = [
    [],
    ['abc', 'bcd', 'cde', 'array'],
    ['a', 'aa', 'ab', 'c'],
    ['a']
]


def test_filter_by_prefix():
    for test_case in test_cases:
        actual_result = filter_by_prefix(test_case, 'a')
        assert actual_result == ['abc', 'array'], "Wrong output: " + str(actual_result) + " ! "


# Run the function with every test case
test_filter_by_prefix()
```
This Python script defines a function `filter_by_prefix` that filters an input list of strings based on their prefix. The function takes two arguments: `List[str]`, which is the input list of strings, and `str`, which is the prefix to filter.

The function then iterates through the input list and returns a new list containing only the strings that start with the given prefix. This function is also have a set of test cases to ensure the correctness of the filtering behavior.