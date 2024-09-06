```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Test cases for the function
strings = ['abc', 'bcd', 'cde', 'array', 'item', 'func']
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']
```
This Python script defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. 

The function takes two parameters: `List[str]` which is the input list of strings and `str` which is the prefix string. 

The function returns a new list with all elements from the input list that start with the given prefix. 

The script then creates a test case with a given input list and prefix, and calls the `filter_by_prefix` function with those arguments. 

This script can be used to filter a list of strings for a specific prefix.