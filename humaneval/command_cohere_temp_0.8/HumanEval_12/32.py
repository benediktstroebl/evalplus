```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    else:
        return max(strings, key=len)
```

This code defines a function `longest` that takes a list of strings as input and returns the longest string in the list. If there are multiple strings of the same length, it returns the first one. If the list is empty, it returns `None`. The logic of the function is straightforward: it checks if the list is empty, and since it's impossible to have empty strings in this case, it returns `None`. In addition, the function checks if there is only one element in the list and directly returns it. Otherwise, it returns the result of `max(strings, key=len)`, which finds the maximum string (resorting to the `len` function as the sorting key) in the list and returns it.

This solution covers all the edge cases mentioned in the prompt and will suitably provide the longest string in lists of strings.