```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```

This script defines a function called `filter_by_substring` that takes two arguments: a list of strings and a substring. The function filters the the using the list of strings and returns a new list that contains only the strings that contain the given substring.