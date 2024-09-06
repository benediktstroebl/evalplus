```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Run the function with sample inputs
strings = ['abc', 'bcd', 'cde', 'array', 'hello', 'world']
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)
``` 
This code defines a function `filter_by_prefix` that filters a list of strings based on a given prefix. It uses the filtering technique to iterate over each string and compare if the prefix of the current string is equal to the given prefix.