```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Example usage:
strings = ["abc", "bacd", "cde", "array"]
sub = "a"
result = filter_by_substring(strings, sub)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This code defines a function called **filter_by_substring** that takes a list of strings and a substring as input and returns a new list of strings that contain the given substring. It uses a filter method on each string in the input list and adds the resulting list to the result.