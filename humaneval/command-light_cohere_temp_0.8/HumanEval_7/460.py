```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -end]

#Unit tests
test_filter_by_substring = []
test_strings = ['abc', 'bacd', 'cde', 'array', 'hello']
test_substring = 'a'
test_result = filter_by_substring(test_strings, test_substring)
test_filter_by_substring.assert array and ['abc', 'cde']
test_filter_by_substring. ['hello']
 filtered_hello = filter_by_substring(['hello'], 'hello')
test_filter_by_substring. [None]
```