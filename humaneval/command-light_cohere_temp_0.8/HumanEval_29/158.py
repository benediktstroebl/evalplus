```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function takes a list of strings and a prefix as input and returns a new list that contains only the strings that start with the given prefix. 

For example, given the input ['abc', 'bcd', 'cde', 'array'], 'a', and 'b', the output will be ['abc', 'array'].