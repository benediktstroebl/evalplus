```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```
This Python code defines a function `filter_by_substring` that filters a list of strings based on whether the string contains a given substring. The function takes two inputs: a list of strings `strings` and a substring `substring`. It uses a list comprehension to iterate over the input strings and returns a new list containing only those strings that contain the specified substring. 
For example, if you pass the list ['abc', 'bacd', 'cde', 'array'], ['abc', 'bacd', 'array'] will be returned, since these strings contain the substring 'a'.