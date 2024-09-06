```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Run the function with test strings
strings = ['abc', 'bcd', 'cde', 'array', 'hello']
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']
``` 
This Python code defines a function `filter_by_prefix` that filters a list of strings based on their prefix. The function takes two parameters: a list of strings `strings` and a prefix `prefix`. It uses a list comprehension to iterate over the input strings and checks if each one starts with the given prefix. The function returns a string elements that start with the specified prefix.