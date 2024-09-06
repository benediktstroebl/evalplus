```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.find(substring)]

    # Test cases
    assert filter_by_substring([], 'a'), ['load', 'lock']
    assert filter_by_substring(['abc', 'aac', 'bcd'], 'a'), ['abc', 'aac', 'bcd']
    assert filter_by_substring([ 'abc', 'bcd', 'abc' ], 'a'), ['abc', 'bcd']
    assert filter_by_substring(['abc', 'def', 'ace'], 'a'), ['abc', 'def', 'ace']
 ``` 
This script defines a function called `filter_by_substring` that filters a list of strings based on a given substring. The function uses the process list comprehension to filter the strings and return the new list.