```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This Python code defines a function `filter_by_prefix` that filters a list of strings based on whether the string starts with a given prefix. It uses the `startswith` method in Python strings to check if the prefix is present at the start of each string in the input list. 

The function takes two parameters:
1. Strings: input list of strings
2. string prefix string. 
It returns a list of strings from the input list that starts with the given prefix.