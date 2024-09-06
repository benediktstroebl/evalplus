```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the specified prefix. It uses a list comprehension to iterate through each string in the input list and checks if it starts with the provided prefix using the `startswith` method. If it does, the string is included in the resulting list. If it doesn't, the string is excluded from the list.  This function efficiently solves the problem and provides the expected output for the given tests.