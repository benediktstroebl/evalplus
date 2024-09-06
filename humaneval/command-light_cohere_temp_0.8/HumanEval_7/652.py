```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
#Tests
strings = ["abc", "bacd", "cde", "array", "123"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
The output of the code is: ['abc', 'bacd', 'array']
This code provides a self-contained function that filters an input list of strings for a given substring.