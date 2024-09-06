```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Test cases
strings = ['abc', 'bcd', 'cde', 'a', 'array', 'alpha', 'bag']
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)
``` 
This code defines a function called `filter_by_prefix` that takes two parameters - a list of strings and a prefix. Using the list comprehension, the function filters the input list of strings and returns a new list containing only the strings that start with the given prefix.