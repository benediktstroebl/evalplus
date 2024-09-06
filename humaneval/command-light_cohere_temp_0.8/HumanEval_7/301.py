```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Tests
strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This script defines a function called **filter_by_substring** that filters an input list of strings for a given substring. The test case is passed to this function with a sample list of strings and a substring.