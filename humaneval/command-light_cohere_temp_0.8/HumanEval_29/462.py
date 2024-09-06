```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This script defines a function, `filter_by_prefix`, which takes a list of strings and a prefix as input and returns a new list containing only the strings from the input list that start with the given prefix. 

The script also provides test cases to verify the correctness of the function, including:
1. string list with no elements, which should return an empty list.
2. The list with elements elements, which should return a list containing only the prefix element.

3. The list with one or more elements, which should return the list containing only the elements that start with the prefix. 

This function is a self-contained solution that efficiently filters a list of strings based on their prefix.