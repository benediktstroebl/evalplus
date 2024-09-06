```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "text"]
substring = "a"

print(filter_by_substring(strings, substring))  # Output: ['abc', 'bacd', 'array']
```
This code provides a function called `filter_by_substring` that takes two arguments: a list of strings and a substring. It creates a result list that contains the elements of the original list that contain the substring. The output will be a list ['abc', 'bacd', 'array'].