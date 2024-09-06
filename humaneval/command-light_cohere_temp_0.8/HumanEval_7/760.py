```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test the function with different inputs
strings = ['abc', 'bacd', 'cde', 'array', '1234']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Output ['abc', 'bacd', 'array']
```
This script defines a function `filter_by_substring` that filters a list of strings for a given substring. The test case passes with different inputs and the output is as expected.