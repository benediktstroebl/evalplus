Here is a self-contained Python script with a function that filters an input list of strings based on a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.search(substring)]
 searched. string

def test_filter_by_substring(strings: List[str], substring: str) -> None:
    strings.range = ['abc', 'bca', 'cde', 'array', 'a', 'abcd', 'bca', 'cd']
    sub = 'a'
    expected = ['abc', 'bca', 'cd']
    actual = filter_by_substring(strings, sub)
    assert actual == expected
```

This script defines a function **filter_by_substring** that filters an input list of strings based on a given substring. The function works by iterating over the input strings and checking if each string contains the given substring. The test_filter_by_substring function is designed to verify that the **filter_by_substring** function works correctly when given the correct inputs.