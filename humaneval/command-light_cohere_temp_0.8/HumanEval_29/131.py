```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This Python code defines a function named `filter_by_prefix`, which filters a list of strings and returns a new list containing only the elements that start with a specific prefix.  The function takes a input of a list of strings and a prefix string, and uses a list comprehension to iterate over the input strings. 

It uses the `startswith` method to check if each string in the list starts with the given prefix, and then returns a new list containing only those strings that pass the condition.