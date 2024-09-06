```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This code implements a filter_by_prefix function that takes a list of strings and a prefix as input and returns a new list that contains only the strings from the input list that start with the specified prefix. 

It uses the List comprehension and the startsswith method to filter out the strings that match the given prefix. 

It successfully passes the tests as well, by providing the correct output for all valid inputs.