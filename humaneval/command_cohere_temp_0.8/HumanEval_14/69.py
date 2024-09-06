```python
from typing import List
from itertools import accumulate

def all_prefixes(string: str) -> List[str]:
    return list(accumulate([string]))
```
This code defines a function `all_prefixes()` that takes a string as an argument and returns a list of its prefixes, ranging from the shortest to the longest. It utilizes the `accumulate()` function from the `itertools` module to create a list of cumulative prefixes from the input string, where each element represents a prefix of the subsequent element. 
The `typing` module is used for type declarations.