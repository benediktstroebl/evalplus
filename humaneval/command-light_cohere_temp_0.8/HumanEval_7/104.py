Here's the solution:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case 1
strings = ['abc', 'bacd', 'cde', 'array', 'hello']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)  # Output ['abc', 'bacd', 'array']

# Test case 2
strings = ['abc', 'bacd', 'cde', 'array', 'foo']
sub = 'X'
result = filter_by_substring(strings, sub)
print(result)  # Output []
```
This script defines a function `filter_by_substring` that filters an input list of strings based on whether the given substring is present in any element of the list. The function utilizes the`List` to check if the substring exists in each string in the list, and returns the list of strings where the substring is found.