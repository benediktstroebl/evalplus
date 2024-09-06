```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Example usage:
strings = ['abc', 'bcd', 'cde', 'array', 'asdf', 'boolean']
prefix = 'a'

print(filter_by_prefix(strings, prefix))  # Output: ['abc', 'array']
```  This Python code defines a function `filter_by_prefix` that filters a list of strings based on a given prefix. It takes the string for each element in the input list that starts with the provided prefix. 

This function is useful for filtering strings that have a specific prefix, which can be useful for various text-processing tasks.