```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function takes a list of strings and a prefix as arguments and returns a new list containing only the strings from the input list that start with the given prefix. 

It utilizes a list comprehension to filter the strings based on their starting characters, and the **startswith** method from the string built-in module to check if a string starts with a given prefix.