Here is a Python script that contains a self-contained function that filters an input list of strings for ones that contain a given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function
strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This script defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list of strings that contain the substring. 

The function uses a list comprehension to iterate through the input list and filter out the strings that contain the given substring.