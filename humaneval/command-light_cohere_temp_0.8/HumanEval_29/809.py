```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Test case 1
strings = ['abc', 'bcd', 'cde', 'array', 'fore', 'begin']
prefix = 'for'
result = filter_by_prefix(strings, prefix)
print(result)
# Expected Output ['for', 'begin']

# Test case 2
strings = ['a' * 5 ## 
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)
# Expected Output []
``` 
This Python script defines a function `filter_by_prefix` that takes two parameters: a list of strings and a prefix. It uses a filter method to filter out the strings from the input list that start with the specified prefix.