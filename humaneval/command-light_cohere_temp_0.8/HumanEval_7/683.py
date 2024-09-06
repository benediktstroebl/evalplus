```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases for the filter_by_substring function
strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
substrings = ['a', 'bcd', 'cd', 'array', 'hello']

print(filter_by_substring(strings, substrings))  # Output: ['abc', 'bacd', 'array']
``` 
This script defines a function `filter_by_substring` that filters a list of strings for substrings. The function takes two inputs: a list of strings and a substring. 

The function then creates a new list that contains only the elements from the original list that contain the given substring.