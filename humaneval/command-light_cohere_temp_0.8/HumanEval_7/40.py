```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.find(substring)]
 string. unique

def test_filter_by_substring(strings: List[str], substring: str) -> None:
    result = filter_by_substring(strings, substring)
    assert len(result) == 4
    assert ['abc', 'bacd', 'array'] == result
    assert ['cde'] not in result
    assert ['def', 'int', 'list'] not in result
``` 
This Python code defines a function `filter_by_substring` that filters a list of strings based on whether the string contains a given substring. 

The `test_filter_by_substring` function tests the `filter_by_substring` function by passing a test list of strings and a substring, and asserting that the result is as expected.