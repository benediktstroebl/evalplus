```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function with multiple lists of strings and substrings
test_filter = [['abc', 'bacd', 'cde', 'array', 'a', 'bc']
, ['ab', 'd', 'xx', 'ccc']
, ['bcd']
, ['cd']

result = filter_by_substring(test_filter, 'a')
assert set(result) == set(['abc', 'bacd', 'array'])
```