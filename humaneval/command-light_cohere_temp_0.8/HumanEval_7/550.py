```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function with a single input list and a substring
strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']

# Test the function with a substring within a string in the list
strings = ['This is a test.', 'Testing testing']
substring = 'test'
result = filter_by_substring(strings, substring)
print(result)  # Output: ['Testing testing']
```
This script defines a function `filter_by_substring` that filters a list of strings for a given substring. The function uses a list comprehension to iterate through the input strings and check if each element contains the specified substring. 
The tests demonstrate the approach with both scenarios of passing a list of strings and a substring within a string.