```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Run the function with sample inputs
strings = ['abc', 'bcd', 'cde', 'array', 'hello', 'world']
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)  # Output ['abc', 'array']
``` 
This Python code defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. The function uses the string slicing to check if each string in the list starts with the specified prefix. It returns a string which list containing those strings that match the condition.