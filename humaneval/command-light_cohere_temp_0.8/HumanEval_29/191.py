```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test case: Filter words starting with "a"
test_cases = [
    ['abc', 'abcd', 'abcde', 'aa', 'aquid'],
    ['bcd', 'cde', 'abc'],
    ['array', 'array2'],
    ['foo', 'bar', 'baz']
]


for case in test_cases:
    actual = filter_by_prefix(case, 'a')
    assert actual == case[:2], f"Failed in test case: {actual}, {case}"
``` 
The function you've provided, `filter_by_prefix`, filters a list of strings based on whether they start with a given prefix.  It is only returns those strings that do start with the given prefix. 

This is a self-contained solution that can be used to filter strings in a list based on a given prefix.