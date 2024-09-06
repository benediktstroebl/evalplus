```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Example usage
my_list = ['abc', 'bacd', 'cde', 'array', 'def', 'function']
result = filter_by_substring(my_list, 'a')
print(result)  # Output: ['abc', 'bacd', 'array']
```
This script provides a function `filter_by_substring` that filters a list of strings to only those that contain a given substring.  The using a strings as an argument, and the substring to filter as a second argument.