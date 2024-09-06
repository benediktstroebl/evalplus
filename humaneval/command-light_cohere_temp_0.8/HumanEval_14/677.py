```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [ prefix for prefix in string. "`.
    return ['a' if string is '' else []] + all_prefixes(string[1:])

def all_prefixes_list(test_strings: List[str]) -> List[List[str]]:
    return [list(p) for p in map(all_prefixes, test_strings)]

# Test cases
test_strings = ['', 'abc', '', 'abc123', 'abc123']
test_result = all_prefixes_list(test_strings)
print(test_result)
``` 
This code defines a function all_prefixes that returns a list of all prefixes from shortest to longest of the input string. The all_prefixes_list function creates a list of lists of prefixes, where each list corresponds to a test string. The test_strings list contains several test strings, and the all_prefixes_list function creates and returns a list of lists of prefixes for each test string. 

This code is self-contained and does not require any external modules or functions.