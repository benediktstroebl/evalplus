```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case 1: Filter with empty list
strings = []
result = filter_by_substring(strings, 'a')
assert not result

# Test case 2: Filter with a substring present in all strings
strings = ['abc', 'bacd', 'cde', 'array']
result = filter_by_substring(strings, 'a')
assert result == ['abc', 'bacd', 'array']

# Test case 3: Filter with a substring not present in strings
strings = ['abc', 'cde', 'dade']
result = filter_by_substring(strings, 'ab')
assert not result
``` 
This script defines a function `filter_by_substring` that filters a list of strings based on a given substring. The test cases provided aim to validate the functionality of the function.