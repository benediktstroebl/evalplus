```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This code implements a function called `filter_by_prefix` that filters an input list of strings and returns a new list that includes only the strings that start with a given prefix. 

The function uses the Python list comprehension to iterate over each string in the input list. The condition checks if the string starts with the given prefix, which is achieved by using the `startswith` method of the string and the prefix as arguments. 

In summary, this function is a concise and effective solution to the problem of filtering strings based on a given prefix.