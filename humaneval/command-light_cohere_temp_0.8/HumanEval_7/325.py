```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function with various inputs
strings = ["abc", "bacd", "cde", "array", "hello"]
sub = "a"
result = filter_by_substring(strings, sub)
print(result)  # Output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes two parameters: a list of strings and a substring. The function then uses a `in` operator to check if each string in the input list contains the given substring, and returns the filtered list.