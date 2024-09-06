```python
from typing import List
from itertools import accumulate

def all_prefixes(string: str) -> List[str]:
    return list(accumulate([string]))
```
This code defines a function `all_prefixes()` that takes a string as input and returns a list of its prefixes, ranging from the shortest to the longest. It utilizes the `accumulate()` function from the `itertools` module to calculate the cumulative prefixes, converting them into a list using the `list()` function. This approach ensures that the prefixes are generated in the desired order.