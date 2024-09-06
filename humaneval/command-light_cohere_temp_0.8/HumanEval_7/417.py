Here is a self-contained Python script that solves the problem of filtering an input list of strings for those that contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]

# Test the function
strings = ['abc', 'bacd', 'cde', 'array', 'hello']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This script defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list containing only the strings that contain the given substring. The test case demonstrates the result by filtering a list of strings and displaying the filtered list.