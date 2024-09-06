```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Test cases
strings = ['abc', 'bcd', 'cde', 'a', 'array', 'begin']
prefix = 'a'

# Function call
result = filter_by_prefix(strings, prefix)

# Print results
print(result)  # Output: ['abc', 'array']
``` 
This Python script defines a function `filter_by_prefix` that filters an input list of strings based on their prefix. 

The function takes two parameters: a list of strings (`strings`) and a prefix string (`prefix`). It returns a new list containing only the strings from the input list that start with the given prefix. 

It achieves this by using a list comprehension with the `startswith` method, which checks if each string in the input list starts with the given prefix.