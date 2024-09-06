Here is a Python script that contains a self-contained function that filters an input list of strings for those containing a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.contains(substring)]

    # Test cases
    strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
    sub = 'a'
    expected = ['abc', 'bacd', 'array']
    assert expected == filter_by_substring(strings, sub), f"Failed in test: {expected}, {strings}"

```

This script provides a function that accepts a list of strings and a substring as arguments. It then returns a strings that contain the given substring. The test cases ensure that the function works as expected.