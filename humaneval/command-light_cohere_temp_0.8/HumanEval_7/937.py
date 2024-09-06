```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Example usage:
strings = ['abc', 'bacd', 'cde', 'array', 'hello']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This code defines a function **filter_by_substring** that takes two arguments: a list of strings and a substring. The function uses a list comprehension to filter the strings that contain the given substring, returning a new list with the matching strings.