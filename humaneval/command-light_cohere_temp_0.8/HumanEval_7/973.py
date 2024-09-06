```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Testing the function
strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```