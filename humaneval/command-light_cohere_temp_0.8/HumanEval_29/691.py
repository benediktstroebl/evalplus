```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

The code defines a function `filter_by_prefix` that takes in a list of strings and a prefix as input. It returns a only the strings from the input list that start with the given prefix, which can be used to filter out specific strings. 

This function uses the typing module for type hinting and better code readability.