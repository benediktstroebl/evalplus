```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Testing the function
strings = ['abc', 'bacd', 'cde', 'array', 'welcome', 'world']
substrings = ['a', 'sd']

print(filter_by_substring(strings, substrings))  # Expected output: ['abc', 'bacd', 'array', 'welcome', 'world']
```
The script defines a function `filter_by_substring` that filters a list of strings based on the presence of a given substring. It works by iterating over each string in the list and checking if the given substring exists.