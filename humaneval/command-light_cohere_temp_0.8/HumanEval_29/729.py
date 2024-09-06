```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
Here, we've defined a `filter_by_prefix` function that takes a list of strings and a prefix as input and returns a new list that contains only the strings from the input list that start with the given prefix. 
This function is self-contained and provides the desired filtering operation on the input strings based on the given prefix.