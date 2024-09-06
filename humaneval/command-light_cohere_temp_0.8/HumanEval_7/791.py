Here's the self-contained Python script that solves the problem you described:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test the function:
strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This function, `filter_by_substring`, takes a list of strings and a substring as input and returns a new list of strings that contain the given substring. The solution is self-contained within the function and passes the tests.