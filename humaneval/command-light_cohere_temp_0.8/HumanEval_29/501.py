```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Test case
test_strings = ['abc', 'bcd', 'cde', 'a', 'array', 'punctuation', 'code']
test_prefix = 'a'

result = filter_by_prefix(test_strings, test_prefix)
print(result)  # Output: ['abc', 'array']
```
The function `filter_by_prefix` filters an input list of strings based on a given prefix. It uses the string slicing to check if each string starts with the specified prefix.