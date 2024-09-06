Here is a self-contained Python script that solves the problem of filtering an input list of strings that contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]

# Test cases for function
strings = ['abc', 'bacd', 'cde', 'array', 'hello']
substring = 'a'

result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This script provides a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list containing only the strings that contain the substring. It effectively filters the Additionallyaya a list comprehension approach to achieve this, and the function is tested using a series of test cases.