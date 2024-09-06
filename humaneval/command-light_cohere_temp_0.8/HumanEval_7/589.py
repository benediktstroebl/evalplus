```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function
strings = ['abc', 'bacd', 'cde', 'array', 'xxyy']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This Python code defines a function called `filter_by_substring` that filters a list of strings for a given substring. The function uses a string's characters as a filter, and returns a new list that contains only the strings that contain the specified substring.