```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Test cases
strings = ['abc', 'bcd', 'cde', '11111', 'jkl', 'asdf']
prefix = 'a'

print(filter_by_prefix(strings, prefix))  # Output: ['abc', '11111', 'asdf']
``` 
This function takes a list of strings and a prefix as input and returns a new list containing only the strings that start with the specified prefix. It uses the simple list comprehension to filter the strings.