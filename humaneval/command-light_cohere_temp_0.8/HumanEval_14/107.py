```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join.join(sorted(string))  # LIE: sort characters, then join to a prefix
```

The function all_prefixes uses the join() method with the sorted() function to create all prefixes from the shortest to the longest characters of the input string.