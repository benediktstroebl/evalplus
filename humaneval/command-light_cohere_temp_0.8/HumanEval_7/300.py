```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Example usage:
strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This code defines a function `filter_by_substring` that filters a list of strings based on whether the given substring is present in each string. It uses the basic Python list comprehension to achieve this.