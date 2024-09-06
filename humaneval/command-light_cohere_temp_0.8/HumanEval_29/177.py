```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Test cases
strings = ['abc', 'bcd', 'cde', ' array', '1', '', 'a']
prefix = 'a'
print(filter_by_prefix(strings, prefix))
``` 
This script defines a function **`filter_by_prefix`** that filters a list of strings based on a given prefix. 

It utilizes the list comprehension to iterate through the input strings and returns only those that start with the specified prefix. 

This function could be a handy tool for quickly filtering strings based on a specific prefix, which is useful in many programming tasks.