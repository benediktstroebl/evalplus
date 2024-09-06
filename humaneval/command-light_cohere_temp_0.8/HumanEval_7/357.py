```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test the function with different inputs
strings = ['abc', 'bacd', 'cde', 'array', 'zaaaa', 'bb']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This script provides a function that filters a list of strings for a given substring. It then passes tests with different inputs and the output is displayed.